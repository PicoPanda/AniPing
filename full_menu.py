"""
⏳ Full CLI Interface for AniPing (Enhanced UI/UX)

This file provides a clear and enhanced CLI interface for the whole project.
UI improvements include:
- Screen clearing between menus.
- Colored headers and dividers using ANSI escape codes.
- Clear visual menu structure.

Helper functions for user input (previously provided by menus.py) are defined here.
Hierarchy:
1. Database Initialization
2. Pre-login Menu:
   - Create Account
   - Login
   - View Top Anime (stub)
   - Exit
3. Post-login Menu:
   - Add Anime to Watch List
   - View Watch List
   - Edit Watch List
   - Logout
"""

import os
import sqlite3
import db_init
import db_functions

# ANSI color codes for styling
COLOR_HEADER = "\033[95m"
COLOR_OKBLUE = "\033[94m"
COLOR_OKGREEN = "\033[92m"
COLOR_WARNING = "\033[93m"
COLOR_FAIL = "\033[91m"
COLOR_ENDC = "\033[0m"
DIVIDER = f"{COLOR_OKBLUE}{'='*50}{COLOR_ENDC}"

def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# -----------------------------------------------------------------------------
# Helper functions (replacement for menus.py)
# -----------------------------------------------------------------------------

def create_account_menu(dummy1, dummy2, dummy3):
    """
    Gathers user input for account creation.
    Returns: (username, email, password)
    """
    print("Enter details for new account:")
    username = input("Username: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    return username, email, password

def login_menu():
    """
    Gather user login credentials.
    Returns: (email, password)
    """
    print("Enter your login credentials:")
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    return email, password

def add_anime_menu():
    """
    Prompt user to enter an anime ID.
    Returns: the input value.
    """
    return input("Enter Anime ID to add: ").strip()

def view_top_anime_menu():
    """
    Stub function to display top anime.
    """
    print("Displaying top anime (stub)...")
    # ... more code for displaying top anime could go here ...

def quit_menu():
    """
    Handles quitting the application.
    """
    print("Exiting AniPing. Goodbye!")

# -----------------------------------------------------------------------------
# Pre-Login Functions
# -----------------------------------------------------------------------------

def handle_create_account():
    """
    Handles account creation using the create_account_menu.
    """
    clear_screen()
    print(f"{DIVIDER}\n{COLOR_HEADER}Create Account{COLOR_ENDC}\n{DIVIDER}")
    username, email, password = create_account_menu("", "", "")
    result = db_functions.add_new_user_to_database(username, email, password)
    if result is None:
        print(f"{COLOR_FAIL}Account creation encountered issues or user already exists.{COLOR_ENDC}")
    else:
        print(f"{COLOR_OKGREEN}Account created successfully. Please login to continue.{COLOR_ENDC}")

def handle_login():
    """
    Handles user login. If login is successful, returns the user tuple.
    """
    clear_screen()
    print(f"{DIVIDER}\n{COLOR_HEADER}User Login{COLOR_ENDC}\n{DIVIDER}")
    email, password = login_menu()
    user = db_functions.login_user(email, password)
    if user:
        return user  # Expected user tuple: (user_id, username, email, password)
    else:
        print(f"{COLOR_FAIL}Login failed. Please try again.{COLOR_ENDC}")
        return None

def handle_top_anime():
    """
    Stub for viewing top anime.
    """
    clear_screen()
    print(f"{DIVIDER}\n{COLOR_HEADER}Top Anime{COLOR_ENDC}\n{DIVIDER}")
    view_top_anime_menu()
    input(f"\nPress Enter to return to the main menu...")

# -----------------------------------------------------------------------------
# Post-Login Functions
# -----------------------------------------------------------------------------

def post_login_menu(user):
    """
    Displays the post-login menu.

    Args:
        user (tuple): The logged in user's details.
    """
    user_id = user[0]
    while True:
        clear_screen()
        print(f"{DIVIDER}")
        print(f"{COLOR_HEADER}User Menu - Logged in as {user[1]}{COLOR_ENDC}")
        print(DIVIDER)
        print("1. ➕  Add Anime to Watch List")
        print("2. 📋  View Watch List")
        print("3. ✏️  Edit Watch List")
        print("4. 🚪  Logout")
        print(DIVIDER)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            clear_screen()
            print(f"{DIVIDER}\n{COLOR_HEADER}Add Anime to Watch List{COLOR_ENDC}\n{DIVIDER}")
            mal_id = add_anime_menu()
            try:
                mal_id = int(mal_id)
            except ValueError:
                print(f"{COLOR_WARNING}Invalid anime ID, please enter a numeric value.{COLOR_ENDC}")
                input("Press Enter to continue...")
                continue
            if db_functions.add_anime_to_watch_list(user_id, mal_id, episodes_watched=0, status="Watching"):
                print(f"{COLOR_OKGREEN}Anime added successfully to your watch list.{COLOR_ENDC}")
            input("Press Enter to continue...")

        elif choice == "2":
            clear_screen()
            print(f"{DIVIDER}\n{COLOR_HEADER}Your Watch List{COLOR_ENDC}\n{DIVIDER}")
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM user_watch_list WHERE user_id=?", (user_id,))
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("Your watch list is empty.")
            conn.close()
            input("\nPress Enter to continue...")

        elif choice == "3":
            clear_screen()
            print(f"{DIVIDER}\n{COLOR_HEADER}Edit Watch List{COLOR_ENDC}\n{DIVIDER}")
            try:
                mal_id = int(input("Enter the Anime ID to update: ").strip())
                episodes = int(input("Enter new episodes watched: ").strip())
            except ValueError:
                print(f"{COLOR_WARNING}Invalid numeric input. Please try again.{COLOR_ENDC}")
                input("Press Enter to continue...")
                continue
            status = input("Enter new status (e.g., Watching, Completed): ").strip()
            if db_functions.update_user_watch_list(user_id, mal_id, episodes, status):
                print(f"{COLOR_OKGREEN}Watch list updated successfully.{COLOR_ENDC}")
            else:
                print(f"{COLOR_WARNING}No matching record found or update failed.{COLOR_ENDC}")
            input("Press Enter to continue...")

        elif choice == "4":
            print(f"{COLOR_OKBLUE}Logging out...{COLOR_ENDC}")
            input("Press Enter to return to the main menu...")
            break
        else:
            print(f"{COLOR_WARNING}Invalid choice, please try again.{COLOR_ENDC}")
            input("Press Enter to continue...")

# -----------------------------------------------------------------------------
# Main Menu Loop (Pre-login)
# -----------------------------------------------------------------------------

def main_cli():
    """
    Main CLI loop that first initializes the database then displays the pre-login menu.
    """
    db_init.init_database()

    while True:
        clear_screen()
        print(f"{DIVIDER}")
        print(f"{COLOR_HEADER}Welcome to AniPing 🎌{COLOR_ENDC}")
        print(DIVIDER)
        print("1. 📝  Create Account")
        print("2. 🔐  Login")
        print("3. 📺  View Top Anime")
        print("4. 🚪  Exit")
        print(DIVIDER)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            handle_create_account()
            input("\nPress Enter to return to the main menu...")
        elif choice == "2":
            user = handle_login()
            if user:
                post_login_menu(user)
        elif choice == "3":
            handle_top_anime()
        elif choice == "4":
            quit_menu()
            break
        else:
            print(f"{COLOR_WARNING}Invalid option. Please try again.{COLOR_ENDC}")
            input("Press Enter to continue...")

# Inlined quit_menu definition (used in main_cli)
def quit_menu():
    """
    Handles quitting the application.
    """
    print("Exiting AniPing. Goodbye!")

# -----------------------------------------------------------------------------
# Entry Point
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main_cli()
