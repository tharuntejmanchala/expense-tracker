# 💸 Expense Tracker

A simple web application to track your daily expenses using **Python Flask** and **MySQL**. Easily add, view, edit, and delete your expenses through a user-friendly interface.

---

## 🚀 Features

- ✅ Add new expenses (date, amount, category, note)
- 📋 View all expenses in a table
- ✏️ Edit and 🗑️ delete individual entries
- 🔍 Filter by category and month
- 📱 Mobile-friendly UI using Bootstrap 5

---

## 🛠 Tech Stack

- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript  
- **Backend**: Python (Flask)  
- **Database**: MySQL  
- **Config Management**: Python Dotenv (`.env`)

---

## 📁 Project Structure

```
expense-tracker/
├── app.py
├── .env
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate       # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root directory

```
MYSQL_HOST=localhost
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=expense_db
```

### 5. Set up the MySQL database

```sql
CREATE DATABASE expense_db;

USE expense_db;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    category VARCHAR(255) NOT NULL,
    note TEXT
);
```

### 6. Run the Flask server

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
