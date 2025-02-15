"""
This file contains the functions that interact with the database.

The functions in this file are used to:
1. Create a new user account
2. Login an existing user
3. Add anime to the user's watch list
4. View the user's watch list
5. Edit the user's watch list

"""

import sqlite3
import os
from api_functions import *

# ✅
def add_new_user_to_database(username, email, password):
    """
    Add a new user to the database. Basically storing MAL account details.
    :param username: The username of the new user
    :param email: The email of the new user
    :param password: The password of the new user
    """
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # Check if the user already exists
    cur.execute("SELECT * FROM user_data WHERE email=?", (email,))
    user = cur.fetchone()

    if user:
        print(f"❌ User {username} already exists!")
        return

    # Add the new user to the database
    cur.execute("INSERT INTO user_data (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()

    print("✅ User added successfully!")

    return True if user else False

# ✅
def login_user(email, password):
    """
    Login an existing user.
    :param email: The email of the user
    :param password: The password of the user

    :return: True if the login is successful, False otherwise
    """
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # Check if the email exists in the database
    cur.execute("SELECT * FROM user_data WHERE email=?", (email,))
    user_email = cur.fetchone()

    if not user_email:
        print("❌ Email not found. Please create an account.")
        conn.close()
        return False
    
    # Check if the password exists in the database
    cur.execute("SELECT * FROM user_data WHERE password=?", (password,))
    user_password = cur.fetchone()

    # Assuming that the user's password is the third field in the table (index 2)
    if not user_password:
        print("❌ Wrong password. Please try again.")
        conn.close()
        return False
    
    # Get the username of the user that is logging in
    cur.execute("SELECT username FROM user_data WHERE email=?", (email,))
    username = cur.fetchone()[0]
    
    print("✅ Login successful!")
    print(f'👋 Welcome back, {username}!')
    print("🔄 Redirecting to the main menu...")

    conn.close()

    return True and user_email

# ✅
def add_anime_to_watch_list(user_id:int, mal_id:int, episodes_watched:int, status:str):
    """
    Add an anime to the user's watch list.
    :param mal_id: The mal_id of the anime
    :param user_email: The email of the user in db
    :param episodes_watched: The episodes watched by the user
    :param status: The status of the anime (e.g. Watching, Completed, Dropped, Re-watching, etc.)
    """

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # Check if the anime is already in the user's watch list
    cur.execute("SELECT * FROM user_watch_list WHERE mal_id=? AND user_id=?", (mal_id, user_id))
    anime = cur.fetchone()

    if anime:
        print("⚠️ Anime already in watch list.")
        return False

    # Add the anime to the user's watch list
    try:
        cur.execute("INSERT INTO user_watch_list (user_id, mal_id, episodes_watched, status) VALUES (?, ?, ?, ?)", (user_id, mal_id, episodes_watched, status))
        conn.commit()
        print("✅ Anime added to watch list successfully!")
        return True

    except sqlite3.Error as e:
        print(f"❌ Error adding anime to watch list: {e}\nValues: mal_id={mal_id}, user_id={user_id}, episodes_watched={episodes_watched}, status={status}")
        conn.rollback()
        return False
    finally:
        conn.close()

    return True

# ✅
def update_user_watch_list(user_id:int, mal_id:int, episodes_watched:int, status:str):
    """
    Update the user's watch list with the episodes, and status.
    :param mal_id: The mal_id of the anime
    :param user_email: The email of the user in db
    :param episodes_watched: The episodes watched by the user
    :param status: The status of the anime (e.g. Watching, Completed, Dropped, Re-watching, etc.)
    """

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    
    # Update the user's watch list
    try:
        cur.execute("""
        UPDATE user_watch_list
        SET episodes_watched = ?, status = ?
        WHERE mal_id = ? AND user_id = ?
        """,
        (episodes_watched, status, mal_id, user_id)
        )

        if cur.rowcount == 0:  # Check if the update affected any rows
            print("⚠️ No matching record found. Update skipped.")
            return False
        
        conn.commit()
        print("Watch list updated successfully!")

        return True

    except sqlite3.Error as e:
        print(f"❌ Error updating watch list: {e}\nValues: mal_id={mal_id}, user_id={user_id}, episodes_watched={episodes_watched}, status={status}")
        conn.rollback()
        return False
    finally:
        conn.close()

    return True

# ✅
def init(db_path="database.db"):
    """
    Initialize the database:
    1. Check if the database already exists.
    2. Create the database and necessary tables if it does not exist.
    3. If the database exists, print a message prompting the user if they want to delete the database.
    4. Create the user_watch_list table that tracks the episodes watched by the user.
    """

    print("Initializing the database...")
    print(f"Database path: '{db_path}'\n")

    db_exists = os.path.exists(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    if not db_exists:
        # Create anime_info table that stores the information of the anime
        cur.execute("""
    CREATE TABLE IF NOT EXISTS anime_info (
        mal_id INTEGER PRIMARY KEY UNIQUE,
        url TEXT,
        image_url TEXT,
        small_image_url TEXT,
        large_image_url TEXT,
        title TEXT,
        title_english TEXT,
        title_japanese TEXT,
        title_synonyms TEXT, -- JSON encoded list
        episodes INTEGER,
        status TEXT,
        airing INTEGER, -- use 0/1 for False/True
        aired_from TEXT,
        aired_to TEXT,
        aired_string TEXT,
        duration TEXT,
        rating TEXT,
        score REAL,
        scored_by INTEGER,
        synopsis TEXT,
        background TEXT,
        season TEXT,
        year INTEGER,
        broadcast_day TEXT,
        broadcast_time TEXT,
        broadcast_timezone TEXT,
        broadcast_string TEXT,
        studios TEXT,        -- JSON encoded list of dicts
        genres TEXT,         -- JSON encoded list of dicts
        streaming TEXT,       -- JSON encoded list of dicts
        watching_users TEXT  -- JSON encoded list of dicts
    )
""")
        # Create user_data table that stores the user information
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                email TEXT UNIQUE,
                password TEXT
            )
        """)
        conn.commit()
        print("Database and tables created successfully.")

        # Create user_watch_list table that tracks the episodes watched by the user
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user_watch_list (
                user_id INTEGER,
                mal_id INTEGER,
                episodes_watched INTEGER DEFAULT 0,
                status TEXT DEFAULT "Watching",
                FOREIGN KEY (user_id) REFERENCES user_data(user_id),
                FOREIGN KEY (mal_id) REFERENCES anime_info(mal_id),
                PRIMARY KEY (user_id, mal_id)
            )
        """)
    else:
        print("Database already exists.")
        delete = input("Do you want to delete the existing database and create a new one? (y/n) : ").lower()
        if delete == 'y':
            print("Deleting the existing database...")
            conn.close()
            os.remove(db_path)
            init_database()
            return
        else:
            print("Exiting without deleting the database.")
            return
    
    conn.close()