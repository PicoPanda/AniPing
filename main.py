from menus import *

def main():

    # Pre-logging menu
    choice = main_menu()
    if choice == "1":
        # Let user create an account, return username, password, email
        create_account_menu()
        new_user = create_account_menu(username)
        new_password = create_account_menu(password)
        new_email = create_account_menu(email)

        # Add new user to the database

    elif choice == "2":
        login_menu()
    elif choice == "3":
        print("View top 5 anime of the week/month")
    elif choice == "4":
        print("Exiting...")


if __name__ == "__main__":
    while True:
        main()
    

