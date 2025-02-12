'''
This file contains the menus for the cli application.

1. Create an account
2. Login
3. View top 5 anime of the week/month
4. 
'''

def clear_screen():
    print("\033c", end="")

def header(menu_name=str):
    clear_screen()
    print("=" * 20)
    print(menu_name)
    print("=" * 20)

def main_menu():
    clear_screen()
    header("👋 Welcome to AniPing!")

    print("1. 📝 Create an account")
    print("2. 🔑 Login")
    print("3. 📊 View top 5 anime of the week/month")
    print("4. 🚪 Exit")
    print("=" * 20)
    print()

    choice = input("Enter your choice: ")
    print(choice)

def create_account_menu(username, email, password):
    clear_screen()
    header("📝 Create an account")

    while True:
        username = input("Enter your username: ")
        if username.isalnum():
            break
        else:
            print("Username should only contain letters and numbers. Please try again.")

    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            break
        else:
            print("Please enter a valid email address.\n")

    while True:
        password = input("Enter your password: ")
        if len(password) >= 6:
            break
        else:
            print("Password should be at least 6 characters long. Please try again.")

    print()

    print("✅ Account created successfully!\n")
    print("🔑 Please login to continue.")
    print("↩️ Press 'Enter' return to the main menu.")
    print("=" * 20)
    print(username, email, password)

    return username, email, password

def login_menu():
    header("🔑 Login")

    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            break
        else:
            print("Please enter a valid email address.\n")

    while True:
        password = input("Enter your password: ")
        if len(password) >= 6:
            break
        else:
            print("Password should be at least 6 characters long. Please try again.")

    print("🔄 Trying to login...")
    print("⏳ Please wait...\n")

    print("=" * 20)
    print(email, password)

    return email, password

def login_failure_menu():
    header("❌ Login failed!")

    print("1. 🔄 Try again")
    print("2. ↩️ Go back")
    print("=" * 20)
    print()

    choice = input("Enter your choice: ")
    print(choice)

def login_success_menu():
    header("✅ Login successful!")

    print("1. ➕ Add anime to watch list")
    print("2. 📋 View watch list")
    print("3. ✏️ Edit watch list")
    print("4. 🚪 Exit (logout)")
    print("=" * 20)
    print()

    choice = input("Enter your choice: ")
    print(choice)

def add_anime_menu():
    header("Add anime to watch list")

    user_mal_id = input("Enter the ID of the anime you want to add: ")

    print()
    print("=" * 20)
    print(user_mal_id)

    return user_mal_id

def view_user_watch_list_menu():
    header("View watch list")

    print("1. View all anime in watch list")
    print("2. View anime by genre")
    print("3. Go back")
    print("=" * 20)
    print()

    choice = input("Enter your choice: ")
    print(choice)

def view_top_anime_menu():
    header("Top 5 anime of the week/month")

    print("1. View top 5 anime of the week")
    print("2. View top 5 anime of the month")
    print("3. Go back")
    print("=" * 20)
    print()

    choice = input("Enter your choice: ")
    print(choice)

def quit_menu():
    print("🙏 Thank you for using AniPing!")
    print("👋 Goodbye!")

login_menu()

