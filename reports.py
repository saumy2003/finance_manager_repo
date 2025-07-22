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
