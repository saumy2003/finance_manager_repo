# transactions.py

import datetime
from database import get_connection

def add_transaction(user_id):
    print("\n➕ Add New Transaction")
    t_type = input("Type (income/expense): ").strip().lower()
    if t_type not in ['income', 'expense']:
        print("❗ Invalid type. Must be 'income' or 'expense'.")
        return

    category = input("Category (e.g., Food, Rent, Salary): ").strip()
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("❗ Invalid amount.")
        return
    date = input("Date (YYYY-MM-DD) [default: today]: ").strip()
    if not date:
        date = datetime.date.today().isoformat()
    note = input("Note (optional): ").strip()

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO transactions (user_id, type, category, amount, date, note)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, t_type, category, amount, date, note))
        conn.commit()
        print("✅ Transaction added successfully.")

def view_transactions(user_id):
    print("\n📄 Your Transactions")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, type, category, amount, date, note
            FROM transactions
            WHERE user_id = ?
            ORDER BY date DESC
        ''', (user_id,))
        rows = cursor.fetchall()
        if not rows:
            print("No transactions found.")
            return
        for row in rows:
            print(f"ID: {row[0]} | {row[1].capitalize()} | {row[2]} | ₹{row[3]} | {row[4]} | {row[5]}")

def delete_transaction(user_id):
    view_transactions(user_id)
    tid = input("\nEnter Transaction ID to delete: ")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions WHERE id = ? AND user_id = ?", (tid, user_id))
        conn.commit()
        if cursor.rowcount:
            print("✅ Transaction deleted.")
        else:
            print("❌ Transaction not found or access denied.")

def update_transaction(user_id):
    view_transactions(user_id)
    tid = input("\nEnter Transaction ID to update: ")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE id = ? AND user_id = ?", (tid, user_id))
        row = cursor.fetchone()
        if not row:
            print("❌ Transaction not found or access denied.")
            return

    print("\nLeave fields blank to keep current values.")
    new_type = input(f"Type ({row[2]}): ") or row[2]
    new_cat = input(f"Category ({row[3]}): ") or row[3]
    new_amount = input(f"Amount ({row[4]}): ") or str(row[4])
    new_date = input(f"Date ({row[5]}): ") or row[5]
    new_note = input(f"Note ({row[6]}): ") or row[6]

    try:
        new_amount = float(new_amount)
    except ValueError:
        print("❗ Invalid amount.")
        return

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE transactions
            SET type = ?, category = ?, amount = ?, date = ?, note = ?
            WHERE id = ? AND user_id = ?
        ''', (new_type, new_cat, new_amount, new_date, new_note, tid, user_id))
        conn.commit()
        print("✅ Transaction updated successfully.")
