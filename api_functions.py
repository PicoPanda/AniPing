"""
This file contains the functions that are used to interact with the API.

We are using Jikan API to get the data of the anime (and manga)
"""

import requests # type: ignore
import json
import os
import time
from datetime import datetime
import pprint

# Constants
BASE_URL = "https://api.jikan.moe/v4"
WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']



def get_anime_info(mal_id=int):
    """
    This function gets the details of a specific anime,
    JIKAN API v4.0.0 ENDPOINT: /anime/{id}/full
    :param anime_id: The ID of the anime for which the details are required,

    :return: The details of the corresponding anime, as a dict.
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

# get_anime_info(9919)

# print(get_anime_schedule(mal_id=9919, day="monday"))







# def get_anime_schedule(mal_id=None, day=None):
    """
    This function gets the schedule of all airing anime,
    JIKAN API v4.0.0 ENDPOINT: /schedules
    :param mal_id: The ID of the anime for which the schedule is required, None returns the schedule for all anime,
    :param day: The day of the week for which the schedule is required, None returns the schedule for the current day,

    :return: The schedule of all corresponding airing anime, as a dict.
    Response can be 200 (success) or 404 (not found)
    """
    try:
        day = day.lower()
    except AttributeError:
        pass
    else:
        if day not in WEEKDAYS:
            raise ValueError("Invalid day of the week provided.")

    params = {
        "filter": day if day is not None and day in WEEKDAYS else None,
        "anime_id": mal_id if isinstance(mal_id, int) and mal_id is not None else None
    }

    if params["filter"] is None:
        print("Getting schedule for the current day...")
    else:
        print(f"Getting schedule for {params['filter']}...")

    if params["anime_id"] is not None and params['anime_id'] >= 0:
        print(f"Getting schedule for anime with ID {params['anime_id']}...\n")
    else:
        print("Getting schedule for all anime...")

    anime_schedule = None
    try:
        response = requests.get(f"{BASE_URL}/schedules", params=params)
        if response.status_code == 200:
            anime_schedule = response.json()
            print("Schedule received successfully!\n")
        else:
            print(f"Error: Received status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    return anime_schedule