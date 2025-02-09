"""
menus.py
--------
Implements the CLI menus for the AniPing application.
Menus included:
 - Main Menu
 - User creation Menu
 - User login Menu
 - Add Anime Menu
 - Update Anime Menu
 - View Anime List Menu
 - Settings Menu (to change name / address / password / notifications)
 - Future Enhancements Menu (to suggest and list future enhancements)
 - About Menu
 - Help Menu
 - Exit Menu
"""

def user_creation_menu():
    print("\n--- User Creation Menu ---")
    # ...logic for creating a user...
    input("Press Enter to return to Main Menu.")

def user_login_menu():
    print("\n--- User Login Menu ---")
    # ...logic for user login...
    input("Press Enter to return to Main Menu.")

def add_anime_menu():
    print("\n--- Add Anime Menu ---")
    # ...logic to add anime...
    input("Press Enter to return to Main Menu.")

def update_anime_menu():
    print("\n--- Update Anime Menu ---")
    # ...logic to update anime...
    input("Press Enter to return to Main Menu.")

def view_anime_list_menu():
    print("\n--- View Anime List Menu ---")
    # ...logic to display user's anime list...
    input("Press Enter to return to Main Menu.")

def settings_menu():
    print("\n--- Settings Menu ---")
    # ...logic to change user settings (name, address, password, notifications)...
    input("Press Enter to return to Main Menu.")

def future_enhancements_menu():
    print("\n--- Future Enhancements Menu ---")
    # ...logic to suggest future enhancements and list them...
    input("Press Enter to return to Main Menu.")

def about_menu():
    print("\n--- About Menu ---")
    # ...display about information...
    input("Press Enter to return to Main Menu.")

def help_menu():
    print("\n--- Help Menu ---")
    # ...display help and usage instructions...
    input("Press Enter to return to Main Menu.")

def exit_menu():
    print("\nExiting AniPing2. Goodbye!")
    exit(0)

def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. User Creation")
        print("2. User Login")
        print("3. Add Anime")
        print("4. Update Anime")
        print("5. View Anime List")
        print("6. Settings")
        print("7. Future Enhancements")
        print("8. About")
        print("9. Help")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            user_creation_menu()
        elif choice == "2":
            user_login_menu()
        elif choice == "3":
            add_anime_menu()
        elif choice == "4":
            update_anime_menu()
        elif choice == "5":
            view_anime_list_menu()
        elif choice == "6":
            settings_menu()
        elif choice == "7":
            future_enhancements_menu()
        elif choice == "8":
            about_menu()
        elif choice == "9":
            help_menu()
        elif choice == "0":
            exit_menu()
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main_menu()
