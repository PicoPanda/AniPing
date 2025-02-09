"""
db_operations.py
----------------
Handles database initialization and operations for AniPing2.

Tables:
 - users: Stores user information.
 - anime_list: Stores anime data with fields including id, title, episodes, airing info, ratings, and external URLs.

Functions:
 - database_initialization(): Initializes the database and creates tables.
 - insert_user_to_db(...): Inserts a new user record.
 - insert_anime_to_db(...): Inserts a new anime record from cleaned API data.
 
Refer to docs/documentation.md for further details.
"""

import sqlite3
from sqlite3 import Error
import os
import sys
import logging
import datetime
import time
import json

from api_request import get_data, clean_data

def database_initialization():
    """
    This function initializes the database and creates the tables
        We have two tables:
            1. users
            2. anime_list
        
        users table has the following columns:
            id: INTEGER PRIMARY KEY
            name: TEXT
            email: TEXT
            password: TEXT
            created_at: TEXT

        anime_list table has the following columns:
            id: INTEGER PRIMARY KEY
            mal_id: INTEGER
            user_id: INTEGER
            title: TEXT
            episodes: INTEGER
            user_episode_achievement: INTEGER
            status: TEXT
            airing_status: BOOLEAN
            user_watching_status: TEXT
            aired_from: TEXT
            aired_to: TEXT
            user_score: REAL
            community_score: REAL
            mal_ranking: INTEGER
            synopsis: TEXT
            season: TEXT
            release_year: INTEGER
            broadcast_date: TEXT
            broadcast_timezone: TEXT
            episode_duration: TEXT
            MAL_url: TEXT
            image_url: TEXT
            studios: TEXT
            genres: TEXT
            themes: TEXT
            user_id: INTEGER
            user_watching_status: TEXT
    """
    try:
        conn = sqlite3.connect('AniPing_Database.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                password TEXT,                   
                created_at TEXT)''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS anime_list (
                id INTEGER PRIMARY KEY, 
                mal_id INTEGER UNIQUE,
                user_id INTEGER, 
                title TEXT, 
                episodes INTEGER, 
                user_episode_achievement INTEGER, 
                status TEXT, 
                airing_status BOOLEAN, 
                user_watching_status TEXT,
                aired_from TEXT, 
                aired_to TEXT, 
                user_score REAL, 
                community_score REAL, 
                mal_ranking INTEGER, 
                synopsis TEXT, 
                season TEXT, 
                release_year INTEGER, 
                broadcast_date TEXT, 
                broadcast_timezone TEXT, 
                episode_duration TEXT, 
                MAL_url TEXT, 
                image_url TEXT, 
                studios TEXT,
                genres TEXT,
                themes TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')

        conn.commit()
        conn.close()
    except Error as e:
        logging.error("Error in database initialization: " + str(e))
        sys.exit(1)
    else:
        print("Database initialized successfully.")

def insert_user_to_db(name, email, password):
    """
    This function inserts a new user to the users table in the database
    """
    try:
        conn = sqlite3.connect('AniPing_Database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users(name, email, password, created_at) VALUES(?, ?, ?, ?)
        ''', (name, email, password, datetime.datetime.now()))
        conn.commit()
        conn.close()
    except Error as e:
        logging.error("Error in inserting user to database: " + str(e))
        sys.exit(1)
    else:
        print("User inserted successfully.")

def insert_anime_to_db(cleaned_data, user_episode_achievement=0, user_watching_status="Watching", user_score=0, user_id=0):
    """
    This function inserts a new anime to the anime_list table in the database
    """   
    if user_score is None:
        user_score = None

    try:
        conn = sqlite3.connect('AniPing_Database.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO anime_list (
            mal_id, title, episodes, user_episode_achievement, status, 
            airing_status, aired_from, aired_to, user_score, community_score, 
            MAL_ranking, synopsis, season, release_year, broadcast_date, 
            broadcast_timezone, episode_duration, MAL_url, image_url, studios, genres, themes, user_id, user_watching_status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (
            cleaned_data["mal_id"], cleaned_data["title"], cleaned_data["episodes"], user_episode_achievement, cleaned_data["status"], 
            cleaned_data["airing_status"], cleaned_data["aired_from"], cleaned_data["aired_to"], user_score, 
            cleaned_data["community_score"], cleaned_data["MAL_ranking"], cleaned_data["synopsis"], cleaned_data["season"], 
            cleaned_data["release_year"], cleaned_data["broadcast_date"], cleaned_data["broadcast_timezone"], 
            cleaned_data["episode_duration"], cleaned_data["MAL_url"], cleaned_data["image_url"], cleaned_data["studios"], 
            cleaned_data["genres"], cleaned_data["themes"], user_id, user_watching_status
        ))

        conn.commit()
        conn.close()
    except Error as e:
        logging.error("Error in inserting anime to database: " + str(e))
        sys.exit(1)

def view_user_anime_list(user_id):
    """
    This function retrieves the anime list of a user and returns it as a list of dictionaries
    """
    try:
        conn = sqlite3.connect('AniPing_Database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM anime_list WHERE user_id = ?
        ''', (user_id,))
        rows = cursor.fetchall()
        conn.close()
        
        anime_list = []
        for row in rows:
            anime = {
                "id": row[0],
                "mal_id": row[1],
                "user_id": row[2],
                "title": row[3],
                "episodes": row[4],
                "user_episode_achievement": row[5],
                "status": row[6],
                "airing_status": row[7],
                "user_watching_status": row[8],
                "aired_from": row[9],
                "aired_to": row[10],
                "user_score": row[11],
                "community_score": row[12],
                "mal_ranking": row[13],
                "synopsis": row[14],
                "season": row[15],
                "release_year": row[16],
                "broadcast_date": row[17],
                "broadcast_timezone": row[18],
                "episode_duration": row[19],
                "MAL_url": row[20],
                "image_url": row[21],
                "studios": row[22],
                "genres": row[23],
                "themes": row[24]
            }
            anime_list.append(anime)
    except Error as e:
        logging.error("Error in retrieving anime list from database: " + str(e))
        sys.exit(1)
    else:
        return anime_list
    
if __name__ == "__main__": # run for test unit

    database_initialization()
    
   # insert_user_to_db('louis','celiankouame@gmail.com', 123456)

    insert_anime_to_db(clean_data(get_data(20)), user_id=1 ) # Naruto
    insert_anime_to_db(clean_data(get_data(52991)), user_id=1 ) # SS no frieren
    insert_anime_to_db(clean_data(get_data(9919)), user_id=1 ) # AO no Exorcist
    insert_anime_to_db(clean_data(get_data(20)), user_id=1 ) # AO no Exorcist

    print(view_user_anime_list(1)) # Louis