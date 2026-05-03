import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from groq import Groq

# -----------------------
# UI CONFIG
# -----------------------
st.set_page_config(page_title="AI Data Analyst", layout="wide")
st.title("📊 AI SQL Data Analyst Agent")

# -----------------------
# API KEY INPUT
# -----------------------
api_key = st.text_input("Enter Groq API Key:", type="password")

if not api_key:
    st.warning("Please enter your API key")
    st.stop()

client = Groq(api_key=api_key)

# -----------------------
# FILE UPLOAD
# -----------------------
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Clean column names
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    st.subheader("📁 Data Preview")
    st.dataframe(df.head())

    # -----------------------
    # STORE IN DATABASE
    # -----------------------
    conn = sqlite3.connect("data.db")
    df.to_sql("data", conn, if_exists="replace", index=False)

    # -----------------------
    # USER QUESTION
    # -----------------------
    question = st.text_input("💬 Ask a question")

    if question:
        with st.spinner("Generating SQL... 🤖"):

            prompt = f"""
            You are an expert SQL analyst.

            Table name: data
            Columns: {list(df.columns)}

            Rules:
            - Use only these columns
            - Use SQLite syntax
            - If revenue needed, use price * quantity
            - Return ONLY SQL query (no explanation)

            Question: {question}
            """

            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}]
                )

                sql_query = response.choices[0].message.content.strip()

                st.subheader("🧠 Generated SQL")
                st.code(sql_query, language="sql")

                # -----------------------
                # EXECUTE QUERY
                # -----------------------
                result = pd.read_sql_query(sql_query, conn)

                st.subheader("📊 Result")
                st.dataframe(result)

                # -----------------------
                # VISUALIZATION
                # -----------------------
                if len(result.columns) >= 2:
                    st.subheader("📈 Visualization")

                    fig = px.bar(
                        result,
                        x=result.columns[0],
                        y=result.columns[1],
                        title="Result Visualization"
                    )
                    st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.error(f"❌ Error: {e}")
