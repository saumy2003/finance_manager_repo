# # budget.py

# from database import get_connection

# def set_budget(user_id):
#     print("\n💰 Set Budget")
#     category = input("Category (e.g., Food, Rent): ").strip()
#     month = input("Month (1-12): ").strip()
#     year = input("Year (YYYY): ").strip()

#     try:
#         amount = float(input("Budget Amount: "))
#     except ValueError:
#         print("❗ Invalid amount.")
#         return

#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             SELECT id FROM budgets
#             WHERE user_id = ? AND category = ? AND month = ? AND year = ?
#         ''', (user_id, category, int(month), int(year)))
#         existing = cursor.fetchone()

#         if existing:
#             cursor.execute('''
#                 UPDATE budgets
#                 SET amount = ?
#                 WHERE id = ?
#             ''', (amount, existing[0]))
#             print("✅ Budget updated.")
#         else:
#             cursor.execute('''
#                 INSERT INTO budgets (user_id, category, amount, month, year)
#                 VALUES (?, ?, ?, ?, ?)
#             ''', (user_id, category, amount, int(month), int(year)))
#             print("✅ Budget set.")

#         conn.commit()

# def check_budgets(user_id, month, year):
#     print(f"\n🧾 Budget Report for {month}/{year}")
#     with get_connection() as conn:
#         cursor = conn.cursor()

#         # Get all budgets for the given month and year
#         cursor.execute('''
#             SELECT category, amount FROM budgets
#             WHERE user_id = ? AND month = ? AND year = ?
#         ''', (user_id, int(month), int(year)))
#         budgets = cursor.fetchall()

#         if not budgets:
#             print("No budgets set for this period.")
#             return

#         for category, limit in budgets:
#             # Sum expenses by category
#             cursor.execute('''
#                 SELECT SUM(amount) FROM transactions
#                 WHERE user_id = ? AND type = 'expense'
#                 AND category = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
#             ''', (user_id, category, f"{int(month):02}", str(year)))
#             total_spent = cursor.fetchone()[0] or 0

#             status = "✅ Within Budget" if total_spent <= limit else "❌ Over Budget"
#             print(f"{category:<15} | Budget: ₹{limit:<8} | Spent: ₹{total_spent:<8} | {status}")



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
    limit = float(input("Monthly Limit: "))
    month = int(input("Month (1-12): "))
    year = int(input("Year (YYYY): "))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT OR REPLACE INTO budgets (user_id, category, limit, month, year)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, category, limit, month, year))
    conn.commit()
    conn.close()
    print("✅ Budget set.")

def check_budgets(user_id):
    month = input("Month (1-12): ")
    year = input("Year (YYYY): ")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT b.category, b.limit, COALESCE(SUM(t.amount), 0)
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
    for category, limit, spent in results:
        print(f"{category}: Spent ₹{spent} / Limit ₹{limit}")
        if spent > limit:
            print("⚠️ Budget exceeded!")
