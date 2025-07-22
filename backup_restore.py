# # backup_restore.py

# import json
# from database import get_connection

# def backup_data(user_id):
#     print("\n📤 Backing up your data...")

#     with get_connection() as conn:
#         cursor = conn.cursor()

#         # Export transactions
#         cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
#         transactions = cursor.fetchall()

#         # Export budgets
#         cursor.execute("SELECT * FROM budgets WHERE user_id = ?", (user_id,))
#         budgets = cursor.fetchall()

#         data = {
#             "transactions": transactions,
#             "budgets": budgets
#         }

#         filename = f"backup_user_{user_id}.json"
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)

#         print(f"✅ Backup completed! Data saved to '{filename}'")

# def restore_data(user_id):
#     print("\n📥 Restore Data")
#     filename = input("Enter backup file name (e.g., backup_user_1.json): ").strip()

#     try:
#         with open(filename, 'r') as f:
#             data = json.load(f)

#         with get_connection() as conn:
#             cursor = conn.cursor()

#             # Restore transactions
#             for tx in data.get("transactions", []):
#                 _, _, t_type, category, amount, date, note = tx
#                 cursor.execute('''
#                     INSERT INTO transactions (user_id, type, category, amount, date, note)
#                     VALUES (?, ?, ?, ?, ?, ?)
#                 ''', (user_id, t_type, category, amount, date, note))

#             # Restore budgets
#             for b in data.get("budgets", []):
#                 _, _, category, amount, month, year = b
#                 cursor.execute('''
#                     INSERT INTO budgets (user_id, category, amount, month, year)
#                     VALUES (?, ?, ?, ?, ?)
#                 ''', (user_id, category, amount, month, year))

#             conn.commit()
#             print("✅ Data restored successfully!")

#     except FileNotFoundError:
#         print("❌ File not found.")
#     except Exception as e:
#         print(f"❌ Failed to restore data: {e}")




import shutil

def backup_data():
    shutil.copyfile('finance_manager.db', 'backup.db')
    print("✅ Backup created as 'backup.db'")

def restore_data():
    shutil.copyfile('backup.db', 'finance_manager.db')
    print("✅ Data restored from 'backup.db'")
