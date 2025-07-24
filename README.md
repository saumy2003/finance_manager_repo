# 🧾 Personal Finance Manager (CLI-based)

---

## 📦 Features

- 🔐 User Registration & Login
- 💰 Add, Update, Delete Transactions
- 📊 Monthly & Yearly Reports
- 📉 Budget Tracking with Alerts
- 💾 Data Backup & Restore (JSON)
- 🧪 Unit Tests for Core Functions

---

🧾 Project Overview
The Personal Finance Manager is a command-line Python application designed to help users manage their personal finances. It allows users to register/login, track income and expenses, manage monthly budgets, view detailed reports, and back up or restore data—all from the terminal.

---
🛠️ Installation Guide

✅ Prerequisites

Python 3.x installed

Git installed

SQLite3 (comes bundled with Python)

GitHub repository (optional for remote backup)

---

💻 Step-by-Step Installation

1. Clone the Repository

git clone https://github.com/your-username/finance_manager_repo.git

cd finance_manager_repo

2. Install Required Packages

This app uses only the Python standard library, so no additional packages are required.

---

🚀 How to Run the Application

From the root of the project folder:

python main.py

You'll see the main menu:

1. Register
2. Login
3. Exit

---

👤 User Registration & Login

📌 Register

Select option 1

Enter a unique username and password

🔐 Login

Select option 2

Enter your registered username and password

---

🧭 Dashboard Menu (After Login)

📊 Dashboard
1. Manage Transactions
2. Manage Budgets
3. View Reports
4. Backup Data
5. Restore Data
6. Logout

---

💵 Manage Transactions

1. Add Income or Expense

Enter amount, category (e.g., salary, groceries), type (income or expense), date, and description.

2. View Transactions

Displays all transactions by date and type.

3. Delete Transaction

Remove any transaction by ID.

---

💡 Manage Budgets

1. Set/Update Budget

Set a monthly spending limit for a specific category.

2. Check Budget Usage

View current month's spending vs budget for each category.

---

📈 View Reports

Monthly and yearly reports with totals for income, expense, and balance.

---

💾 Backup & Restore

1. Backup

Creates a backup file backup_finance_manager.db.

2. Restore

Restores the most recent backup file into the database.

---

🔐 Security Notes

Passwords are stored in hashed format for protection.

Data is stored locally in SQLite DB.

---

🧑‍💻 Author

👤 Developed by: Saumya Prajapati

🌐 GitHub: github.com/saumy2003

---
