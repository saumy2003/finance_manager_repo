# main.py

from database import initialize_database
from auth import register_user, login_user
from transactions import add_transaction, view_transactions, update_transaction, delete_transaction
from reports import get_monthly_report, get_yearly_report, get_category_breakdown
from budget import set_budget, check_budgets
from backup_restore import backup_data, restore_data


def main():
    print("\n🔐 Welcome to Personal Finance Manager 🔐")
    initialize_database()

    user_id = None
    while not user_id:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            user_id = login_user()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid option. Try again.")

    if user_id:
        print(f"➡️ Logged in as user ID {user_id}")
        # Next: Call transaction/dashboard menu here

if __name__ == '__main__':
    main()



def dashboard(user_id):
    while True:
        print("\n💼 Dashboard")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Logout")

        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction(user_id)
        elif choice == '2':
            view_transactions(user_id)
        elif choice == '3':
            update_transaction(user_id)
        elif choice == '4':
            delete_transaction(user_id)
        elif choice == '5':
            print("👋 Logged out.")
            break
        else:
            print("❗ Invalid option.")

def show_reports(user_id):
    print("\n📊 Reports Menu")
    print("1. Monthly Report")
    print("2. Yearly Report")
    print("3. Category Breakdown")
    choice = input("Choose an option: ")

    if choice == '1':
        month = input("Enter month (1-12): ")
        year = input("Enter year (YYYY): ")
        get_monthly_report(user_id, month, year)
    elif choice == '2':
        year = input("Enter year (YYYY): ")
        get_yearly_report(user_id, year)
    elif choice == '3':
        month = input("Enter month (1-12) or leave blank: ")
        year = input("Enter year (YYYY): ")
        if month:
            get_category_breakdown(user_id, month, year)
        else:
            get_category_breakdown(user_id, None, year)
    else:
        print("❗ Invalid option.")


def budget_menu(user_id):
    print("\n💡 Budget Menu")
    print("1. Set or Update Budget")
    print("2. Check Budget Usage")
    choice = input("Choose an option: ")

    if choice == '1':
        set_budget(user_id)
    elif choice == '2':
        month = input("Enter month (1-12): ")
        year = input("Enter year (YYYY): ")
        check_budgets(user_id, month, year)
    else:
        print("❗ Invalid option.")


def backup_restore_menu(user_id):
    print("\n🗃️ Backup & Restore")
    print("1. Backup Data")
    print("2. Restore Data")
    choice = input("Choose an option: ")

    if choice == '1':
        backup_data(user_id)
    elif choice == '2':
        restore_data(user_id)
    else:
        print("❗ Invalid option.")