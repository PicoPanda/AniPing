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
import json
import time
from datetime import datetime
from api_functions import *

def add_new_user_to_database(username, email, password):
    """
    Add a new user to the database.
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

def parse_and_insert_json(json_data):
    """
    Parse JSON data and insert it into the database.
    
    Args:
        json_data (dict): The JSON data to be inserted.
        db_path (str, optional): The path to the SQLite database. Defaults to "database.db".
        user_email (str, optional): The email of the user associated with this data. Defaults to None.
        
    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    # Connect to the database
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    json_data = json_data.get("data", {})
    
    try:
        # Assuming json_data contains anime information
        # Let's extract the required fields for the anime_info table
        mal_id = json_data.get("mal_id")
        url = json_data.get("url")
        image_url = json_data.get("image_url")
        small_image_url = json_data.get("small_image_url")
        large_image_url = json_data.get("large_image_url")
        title = json_data.get("title")
        title_english = json_data.get("title_english")
        title_japanese = json_data.get("title_japanese")
        title_synonyms = json.dumps(json_data.get("title_synonyms", []))
        episodes = json_data.get("episodes")
        status = json_data.get("status")
        airing = 1 if json_data.get("airing") else 0
        aired = json_data.get("aired")
        aired_from = aired.get("from", "N/A")
        aired_to = aired.get("to", "N/A")
        aired_string = aired.get("string", "N/A")
        duration = json_data.get("duration")
        rating = json_data.get("rating")
        score = json_data.get("score", 0.0)
        scored_by = json_data.get("scored_by", 0)
        synopsis = json_data.get("synopsis")
        background = json_data.get("background")
        season = json_data.get("season")
        year = json_data.get("year")
        broadcast = json_data.get("broadcast")
        broadcast_day = broadcast.get("day")
        broadcast_time = broadcast.get("time")
        broadcast_timezone = broadcast.get("timezone")
        broadcast_string = broadcast.get("string")
        
        # Studios, genres, and streaming are lists of dictionaries
        studios = json.dumps(json_data.get("studios", []))
        genres = json.dumps(json_data.get("genres", []))
        streaming = json.dumps(json_data.get("streaming", []))
        
        # Insert into anime_info table
        cur.execute("""
            INSERT INTO anime_info (
                mal_id, url, image_url, small_image_url, large_image_url,
                title, title_english, title_japanese, title_synonyms,
                episodes, status, airing, aired_from, aired_to, aired_string,
                duration, rating, score, scored_by, synopsis, background,
                season, year, broadcast_day, broadcast_time, broadcast_timezone,
                broadcast_string, studios, genres, streaming
            ) VALUES (?, ?, ?, ?, ?,
                      ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                      ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (mal_id, url, image_url, small_image_url, large_image_url,
              title, title_english, title_japanese, title_synonyms,
              episodes, status, airing, aired_from, aired_to, aired_string,
              duration, rating, score, scored_by, synopsis, background,
              season, year, broadcast_day, broadcast_time, broadcast_timezone,
              broadcast_string, studios, genres, streaming))
        conn.commit()

        print("✅ Data inserted successfully!")

    except sqlite3.Error as e:
        print(f"❌ Error inserting data for anime {mal_id}: {e}\n")
        conn.rollback()
        return False
    finally:
        conn.close()
        
        
        return True

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


# add_anime_to_watch_list(1, 5114, 2, "Watching")
# update_user_watch_list(1, 52991, 10, "Watching")

"""
add_new_user_to_database("celian", "test@email.com", "testpassword")
add_new_user_to_database("louis", "test@email.com", "testpassword")
add_new_user_to_database("louis", "test1@email.com", "testpassword")

json_data = get_anime_info(52991) # Sousou no Frieren
parse_and_insert_json(json_data)

json_data = get_anime_info(5114) # FMA: Brotherhood
parse_and_insert_json(json_data)

json_data = get_anime_info(58572) # Shangri La Frontier
parse_and_insert_json(json_data)
add_new_user_to_database("celian", "test@email.com", "testpassword")
add_new_user_to_database("louis", "test@email.com", "testpassword")
add_new_user_to_database("louis", "test1@email.com", "testpassword")


# login_user("test@email.com", "testpassword")
# print(json_data)
"""
