# # # main.py

# # # from database import initialize_database
# # # from auth import register_user, login_user, create_user_table
# # # from transactions import add_transaction, view_transactions, update_transaction, delete_transaction
# # # from reports import get_monthly_report, get_yearly_report, get_category_breakdown
# # # from budget import set_budget, check_budgets
# # # from backup_restore import backup_data, restore_data


# # from auth import create_user_table, register_user, login_user
# # from transaction import transaction_menu
# # from budget import budget_menu
# # from reports import generate_reports

# # def main():
# #     create_user_table()  # Ensure user table exists at start

# #     print("\n🔐 Welcome to Personal Finance Manager 🔐\n")

# #     user_id = None
# #     while True:
# #         print("1. Register")
# #         print("2. Login")
# #         print("3. Exit")
# #         choice = input("Choose an option: ").strip()

# #         if choice == '1':
# #             register_user()
# #         elif choice == '2':
# #             user_id = login_user()
# #             if user_id:
# #                 break
# #         elif choice == '3':
# #             print("👋 Goodbye!")
# #             return
# #         else:
# #             print("❌ Invalid choice. Try again.\n")

# #     # After successful login
# #     while True:
# #         print("\n📊 Dashboard Menu:")
# #         print("1. Manage Transactions")
# #         print("2. Manage Budgets")
# #         print("3. View Reports")
# #         print("4. Logout")
# #         choice = input("Choose an option: ").strip()

# #         if choice == '1':
# #             transaction_menu(user_id)
# #         elif choice == '2':
# #             budget_menu(user_id)
# #         elif choice == '3':
# #             generate_reports(user_id)
# #         elif choice == '4':
# #             print("✅ Logged out successfully.\n")
# #             break
# #         else:
# #             print("❌ Invalid choice. Try again.\n")

# # if __name__ == "__main__":
# #     main()




# # def dashboard(user_id):
# #     while True:
# #         print("\n==== Dashboard ====")
# #         print("1. Add Income/Expense")
# #         print("2. View Transactions")
# #         print("3. Edit Transaction")
# #         print("4. Set Budget")
# #         print("5. View Report")
# #         print("6. Backup Data")
# #         print("7. Restore Data")
# #         print("8. Logout")
# #         choice = input("Enter your choice: ")

# #         if choice == '1':
# #             add_transaction(user_id)
# #         elif choice == '2':
# #             view_transactions(user_id)
# #         elif choice == '3':
# #             delete_transaction(user_id)
# #         elif choice == '4':
# #             update_transaction(user_id)
# #         elif choice == '5':
# #             get_yearly_report(user_id)
# #         elif choice == '6':
# #             get_monthly_report(user_id)
# #         elif choice == '7':
# #             set_budget(user_id)
# #         elif choice == '8':
# #             backup_data(user_id)
# #         elif choice == '9':
# #             restore_data(user_id)
# #         elif choice == '10':
# #             print("✅ Logged out.")
# #             break
# #         else:
# #             print("❌ Invalid choice. Please try again.")


# # def show_reports(user_id):
# #     print("\n📊 Reports Menu")
# #     print("1. Monthly Report")
# #     print("2. Yearly Report")
# #     print("3. Category Breakdown")
# #     choice = input("Choose an option: ")

# #     if choice == '1':
# #         month = input("Enter month (1-12): ")
# #         year = input("Enter year (YYYY): ")
# #         get_monthly_report(user_id, month, year)
# #     elif choice == '2':
# #         year = input("Enter year (YYYY): ")
# #         get_yearly_report(user_id, year)
# #     elif choice == '3':
# #         month = input("Enter month (1-12) or leave blank: ")
# #         year = input("Enter year (YYYY): ")
# #         if month:
# #             get_category_breakdown(user_id, month, year)
# #         else:
# #             get_category_breakdown(user_id, None, year)
# #     else:
# #         print("❗ Invalid option.")


# # def budget_menu(user_id):
# #     print("\n💡 Budget Menu")
# #     print("1. Set or Update Budget")
# #     print("2. Check Budget Usage")
# #     choice = input("Choose an option: ")

# #     if choice == '1':
# #         set_budget(user_id)
# #     elif choice == '2':
# #         month = input("Enter month (1-12): ")
# #         year = input("Enter year (YYYY): ")
# #         check_budgets(user_id, month, year)
# #     else:
# #         print("❗ Invalid option.")


# # def backup_restore_menu(user_id):
# #     print("\n🗃️ Backup & Restore")
# #     print("1. Backup Data")
# #     print("2. Restore Data")
# #     choice = input("Choose an option: ")

# #     if choice == '1':
# #         backup_data(user_id)
# #     elif choice == '2':
# #         restore_data(user_id)
# #     else:
# #         print("❗ Invalid option.")

# from auth import create_user_table, register_user, login_user
# from transaction import create_transaction_table, transaction_menu
# from budget import create_budget_table, budget_menu
# from reports import generate_reports
# from backup_restore import backup_data, restore_data

# def main():
#     # Ensure required tables are created
#     create_user_table()
#     create_transaction_table()
#     create_budget_table()

#     print("\n🔐 Welcome to Personal Finance Manager 🔐\n")

#     # Authentication Loop
#     user_id = None
#     while not user_id:
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Choose an option: ").strip()

#         if choice == '1':
#             register_user()
#         elif choice == '2':
#             user_id = login_user()
#         elif choice == '3':
#             print("👋 Goodbye!")
#             return
#         else:
#             print("❌ Invalid choice. Try again.\n")

#     # Dashboard Loop
#     while True:
#         print("\n📊 Dashboard Menu:")
#         print("1. Manage Transactions")
#         print("2. Manage Budgets")
#         print("3. View Reports")
#         print("4. Backup Data")
#         print("5. Restore Data")
#         print("6. Logout")
#         choice = input("Choose an option: ").strip()

#         if choice == '1':
#             transaction_menu(user_id)
#         elif choice == '2':
#             budget_menu(user_id)
#         elif choice == '3':
#             generate_reports(user_id)
#         elif choice == '4':
#             backup_data(user_id)
#         elif choice == '5':
#             restore_data(user_id)
#         elif choice == '6':
#             print("\n✅ Logged out successfully.\n")
#             break
#         else:
#             print("❌ Invalid option. Please try again.\n")

# if __name__ == "__main__":
#     main()






from auth import register_user, login_user
from transaction import transaction_menu
from budget import budget_menu
from reports import generate_reports
from backup import backup_data, restore_data
from database import init_db

def main():
    init_db()
    print("\n🔐 Welcome to Personal Finance Manager 🔐\n")

    user_id = None
    while not user_id:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            user_id = login_user()
        elif choice == '3':
            print("👋 Goodbye!")
            return

    while True:
        print("\n📊 Dashboard")
        print("1. Manage Transactions")
        print("2. Manage Budgets")
        print("3. View Reports")
        print("4. Backup Data")
        print("5. Restore Data")
        print("6. Logout")

        choice = input("Choose: ")

        if choice == '1':
            transaction_menu(user_id)
        elif choice == '2':
            budget_menu(user_id)
        elif choice == '3':
            generate_reports(user_id)
        elif choice == '4':
            backup_data()
        elif choice == '5':
            restore_data()
        elif choice == '6':
            print("✅ Logged out.")
            break

if __name__ == "__main__":
    main()
