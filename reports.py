# # reports.py

# from database import get_connection

# def get_monthly_report(user_id, month, year):
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             SELECT type, SUM(amount)
#             FROM transactions
#             WHERE user_id = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
#             GROUP BY type
#         ''', (user_id, f"{int(month):02}", str(year)))
#         result = dict(cursor.fetchall())

#     income = result.get('income', 0)
#     expense = result.get('expense', 0)
#     savings = income - expense

#     print(f"\n📅 Monthly Report for {month}/{year}")
#     print(f"Total Income: ₹{income}")
#     print(f"Total Expense: ₹{expense}")
#     print(f"Total Savings: ₹{savings}")

# def get_yearly_report(user_id, year):
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             SELECT type, SUM(amount)
#             FROM transactions
#             WHERE user_id = ? AND strftime('%Y', date) = ?
#             GROUP BY type
#         ''', (user_id, str(year)))
#         result = dict(cursor.fetchall())

#     income = result.get('income', 0)
#     expense = result.get('expense', 0)
#     savings = income - expense

#     print(f"\n📆 Yearly Report for {year}")
#     print(f"Total Income: ₹{income}")
#     print(f"Total Expense: ₹{expense}")
#     print(f"Total Savings: ₹{savings}")

# def get_category_breakdown(user_id, month=None, year=None):
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         if month and year:
#             cursor.execute('''
#                 SELECT category, type, SUM(amount)
#                 FROM transactions
#                 WHERE user_id = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
#                 GROUP BY category, type
#             ''', (user_id, f"{int(month):02}", str(year)))
#         elif year:
#             cursor.execute('''
#                 SELECT category, type, SUM(amount)
#                 FROM transactions
#                 WHERE user_id = ? AND strftime('%Y', date) = ?
#                 GROUP BY category, type
#             ''', (user_id, str(year)))
#         else:
#             return

#         results = cursor.fetchall()
#         if results:
#             print("\n📊 Category-wise Breakdown:")
#             for cat, typ, amt in results:
#                 print(f"{typ.title():<7} | {cat:<15} | ₹{amt}")
#         else:
#             print("No data found for the given period.")



from database import get_db_connection

def generate_reports(user_id):
    print("\n📈 Reports")
    print("1. Monthly Report")
    print("2. Yearly Report")
    print("3. Back")
    choice = input("Choose: ")

    if choice == '1':
        month = input("Month (1-12): ")
        year = input("Year (YYYY): ")
        get_report(user_id, month, year)
    elif choice == '2':
        year = input("Year (YYYY): ")
        get_report(user_id, None, year)
    elif choice == '3':
        return

def get_report(user_id, month, year):
    conn = get_db_connection()
    cur = conn.cursor()

    if month:
        cur.execute('''
            SELECT type, SUM(amount) FROM transactions
            WHERE user_id = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
            GROUP BY type
        ''', (user_id, f'{int(month):02d}', year))
    else:
        cur.execute('''
            SELECT type, SUM(amount) FROM transactions
            WHERE user_id = ? AND strftime('%Y', date) = ?
            GROUP BY type
        ''', (user_id, year))

    data = cur.fetchall()
    conn.close()

    income = expense = 0
    for row in data:
        if row[0] == 'income':
            income = row[1]
        elif row[0] == 'expense':
            expense = row[1]

    print(f"Income: ₹{income or 0}")
    print(f"Expense: ₹{expense or 0}")
    print(f"Savings: ₹{(income or 0) - (expense or 0)}")
