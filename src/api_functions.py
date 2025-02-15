"""
This file contains the functions that are used to interact with the API.

We are using Jikan API to get the data of the anime (and manga)
"""

import requests # type: ignore
import json
import sqlite3

# Constants
BASE_URL = "https://api.jikan.moe/v4"
WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


# ✅
def get_anime_info(mal_id=int):
    """
    This function gets the details of a specific anime,
    JIKAN API v4.0.0 ENDPOINT: /anime/{id}/full
    :param anime_id: The ID of the anime for which the details are required,

    :return: json object containing the details of the anime.

    Response can be 200 (success) or 404 (not found).
    """
    try:
        response = requests.get(f"{BASE_URL}/anime/{mal_id}/full")
        if response.status_code == 200:
            anime_info = response.json()
            print("✅ Anime details received successfully!")
        elif response.status_code == 404:
            print("❌ Error: Anime not found")
            return None
        else:
            print(f"⚠️ Error: Received status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return None

    return anime_info

# ✅
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

# Test
get_anime_info(9919) # returns json object of the anime with the id 9919 from MAL database through Jikan API
print(get_anime_info(9919))