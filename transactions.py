# # transactions.py

# import datetime, sqlite3
# from database import get_connection

# def add_transaction(user_id):
#     print("\n➕ Add New Transaction")
#     t_type = input("Type (income/expense): ").strip().lower()
#     if t_type not in ['income', 'expense']:
#         print("❗ Invalid type. Must be 'income' or 'expense'.")
#         return

#     category = input("Category (e.g., Food, Rent, Salary): ").strip()
#     try:
#         amount = float(input("Amount: "))
#     except ValueError:
#         print("❗ Invalid amount.")
#         return
#     date = input("Date (YYYY-MM-DD) [default: today]: ").strip()
#     if not date:
#         date = datetime.date.today().isoformat()
#     note = input("Note (optional): ").strip()

#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO transactions (user_id, type, category, amount, date, note)
#             VALUES (?, ?, ?, ?, ?, ?)
#         ''', (user_id, t_type, category, amount, date, note))
#         conn.commit()
#         print("✅ Transaction added successfully.")

# def view_transactions(user_id):
#     print("\n📄 --- Your Transactions ---")
#     conn = sqlite3.connect('finance_manager.db')
#     c = conn.cursor()

#     c.execute("SELECT id, amount, type, category, date FROM transactions WHERE user_id=? ORDER BY date DESC", (user_id,))
#     rows = c.fetchall()

#     if not rows:
#         print("No transactions found.")
#     else:
#         print("{:<5} {:<10} {:<10} {:<15} {:<12}".format("ID", "Amount", "Type", "Category", "Date"))
#         print("-" * 60)
#         for row in rows:
#             print("{:<5} {:<10} {:<10} {:<15} {:<12}".format(row[0], row[1], row[2], row[3], row[4]))

#     conn.close()
# def delete_transaction(user_id):
#     view_transactions(user_id)
#     tid = input("\nEnter Transaction ID to delete: ")
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("DELETE FROM transactions WHERE id = ? AND user_id = ?", (tid, user_id))
#         conn.commit()
#         if cursor.rowcount:
#             print("✅ Transaction deleted.")
#         else:
#             print("❌ Transaction not found or access denied.")

# def update_transaction(user_id):
#     view_transactions(user_id)
#     tid = input("\nEnter Transaction ID to update: ")
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM transactions WHERE id = ? AND user_id = ?", (tid, user_id))
#         row = cursor.fetchone()
#         if not row:
#             print("❌ Transaction not found or access denied.")
#             return

#     print("\nLeave fields blank to keep current values.")
#     new_type = input(f"Type ({row[2]}): ") or row[2]
#     new_cat = input(f"Category ({row[3]}): ") or row[3]
#     new_amount = input(f"Amount ({row[4]}): ") or str(row[4])
#     new_date = input(f"Date ({row[5]}): ") or row[5]
#     new_note = input(f"Note ({row[6]}): ") or row[6]

#     try:
#         new_amount = float(new_amount)
#     except ValueError:
#         print("❗ Invalid amount.")
#         return

#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             UPDATE transactions
#             SET type = ?, category = ?, amount = ?, date = ?, note = ?
#             WHERE id = ? AND user_id = ?
#         ''', (new_type, new_cat, new_amount, new_date, new_note, tid, user_id))
#         conn.commit()
#         print("✅ Transaction updated successfully.")




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
