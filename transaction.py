from database import get_db_connection
from datetime import datetime

def transaction_menu(user_id):
    while True:
        print("\n💵 Transaction Menu")
        print("1. Add Income/Expense")
        print("2. View Transactions")
        print("3. Delete Transaction")
        print("4. Back")
        choice = input("Choose: ")

        if choice == '1':
            add_transaction(user_id)
        elif choice == '2':
            view_transactions(user_id)
        elif choice == '3':
            delete_transaction(user_id)
        elif choice == '4':
            break
        else:
            print("❌ Invalid option.")

def add_transaction(user_id):
    amount = float(input("Amount: "))
    category = input("Category: ")
    t_type = input("Type (income/expense): ")
    date = input("Date (YYYY-MM-DD): ")
    desc = input("Description: ")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO transactions (user_id, amount, category, type, date, description)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, amount, category, t_type, date, desc))
    conn.commit()
    conn.close()
    print("✅ Transaction added.")

def view_transactions(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT amount, category, type, date, description FROM transactions WHERE user_id = ?", (user_id,))
    rows = cur.fetchall()
    conn.close()

    print("\n📋 Your Transactions:")
    for row in rows:
        print(row)

def delete_transaction(user_id):
    view_transactions(user_id)
    t_id = int(input("Enter ID to delete: "))
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM transactions WHERE id = ? AND user_id = ?", (t_id, user_id))
    conn.commit()
    conn.close()
    print("✅ Transaction deleted.")
