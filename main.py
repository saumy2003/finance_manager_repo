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
