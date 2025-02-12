"""
This file is used to initialize the whole database.

The database has three tables:
1. anime_info: Contains the information of the anime
2. user_data: Contains the information of the user and their watch list
3.

The functions in this file are used to create the database and tables before first use.
"""

import sqlite3
import os
import json
import time
from datetime import datetime


def init_database(db_path="database.db"):
    """
    Initialize the database:
    1. Check if the database already exists.
    2. Create the database and necessary tables if it does not exist.
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
        print("Database already exists. Delete it to reinitialize.")
    
    conn.close()

if __name__ == "__main__":
    init_database()
