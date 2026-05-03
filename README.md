# AI---SQL-Data-Analyst-Agent
# 📊 AI SQL Data Analyst Agent

## 🚀 Project Overview

The **AI SQL Data Analyst Agent** is an intelligent data analysis application that allows users to interact with their data using natural language. Users can upload a CSV file, ask questions in plain English, and receive accurate insights powered by an AI model.

The system automatically converts user queries into SQL commands, executes them on a database, and presents results along with interactive visualizations.

---

## 🎯 Objective

To simplify data analysis by enabling non-technical users to:

* Query data using natural language
* Automatically generate SQL queries
* Visualize insights without writing code

---

## 🧠 How It Works

1. Upload a CSV file
2. Data is loaded using Pandas
3. Stored in an SQLite database
4. User enters a question
5. AI model converts question → SQL query
6. SQL query is executed
7. Results are displayed with charts

---

##  System Architecture

User Input (CSV + Question)
⬇
Pandas Data Loader
⬇
SQLite Database
⬇
Groq LLM (SQL Generation)
⬇
SQL Execution
⬇
Result + Visualization

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **Database**: SQLite
* **Data Processing**: Pandas
* **Visualization**: Plotly
* **AI Model**: Groq (LLaMA 3 / Mixtral)

---

## ✨ Features

* 📁 Upload any CSV dataset
* 💬 Ask questions in natural language
* 🧠 Automatic SQL query generation
* 📊 Dynamic data visualization (Bar, Pie, Line charts)
* ⚡ Fast and interactive UI
* 🔐 Secure API key input

---

## 📂 Project Structure

```
sql_agent/
│── app.py
│── sales_data.csv
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ▶️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/ai-sql-data-analyst.git
cd ai-sql-data-analyst/sql_agent
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
python -m streamlit run app.py
```

---

## 🔑 API Configuration

* Get your API key from Groq
* Enter it in the app UI when prompted

---

## 📊 Sample Dataset

A sample dataset (`sales_data.csv`) is included for testing.
You can also upload your own CSV file.

---

## 💬 Example Questions

* Total revenue
* Revenue by year
* Top 5 products by sales
* Average price by category
* Sales distribution by city

---

## ⚠️ Common Issues & Fixes

* **Streamlit not found** → `pip install streamlit`
* **Model error** → Use latest Groq model
* **SQL error** → Ensure correct column names
* **No chart** → Ensure query returns at least 2 columns

---

## 🔮 Future Enhancements

* Chat-based conversational UI
* Export results as PDF/Excel
* Advanced analytics (forecasting, trends)
* Multi-table database support

---

## 👩‍💻 Author

Raksha S

---

## 📌 Conclusion

This project demonstrates how AI can simplify data analysis by bridging the gap between natural language and structured query systems. It provides an efficient and user-friendly way to extract insights from raw data.

---

⭐ If you like this project, consider giving it a star!
