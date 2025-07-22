from database import get_db_connection

def budget_menu(user_id):
    print("\n💡 Budget Menu")
    print("1. Set/Update Budget")
    print("2. Check Budget Usage")
    choice = input("Choose: ")

    if choice == '1':
        set_budget(user_id)
    elif choice == '2':
        check_budgets(user_id)

def set_budget(user_id):
    category = input("Category: ")
    monthly_limit = float(input("Monthly Limit: "))
    month = int(input("Month (1-12): "))
    year = int(input("Year (YYYY): "))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT OR REPLACE INTO budgets (user_id, category, monthly_limit, month, year)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, category, monthly_limit, month, year))
    conn.commit()
    conn.close()
    print("✅ Budget set.")

def check_budgets(user_id):
    month = input("Month (1-12): ")
    year = input("Year (YYYY): ")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT b.category, b.monthly_limit, COALESCE(SUM(t.amount), 0)
        FROM budgets b
        LEFT JOIN transactions t ON b.category = t.category AND b.user_id = t.user_id
            AND strftime('%m', t.date) = ? AND strftime('%Y', t.date) = ?
            AND t.type = 'expense'
        WHERE b.user_id = ? AND b.month = ? AND b.year = ?
        GROUP BY b.category
    ''', (f'{int(month):02d}', year, user_id, int(month), int(year)))

    results = cur.fetchall()
    conn.close()

    print("\n📊 Budget Usage:")
    for category, monthly_limit, spent in results:
        print(f"{category}: Spent ₹{spent} / Limit ₹{monthly_limit}")
        if spent > monthly_limit:
            print("⚠️ Budget exceeded!")
