"""
api_request.py
--------------
Handles API requests to the Jikan API.

Functions:
 - get_data(anime_id: int): Retrieves JSON data for an anime.
 - clean_data(anime_data): Normalizes the JSON data into the required format.

Refer to docs/documentation.md for further details.
"""
import requests # type: ignore
import json

def get_data(anime_id:int):
    """
    This function gets the data from the JIKAN API v4.0.0
    """
    # https://docs.api.jikan.moe/

    anime_data = requests.get(f'https://api.jikan.moe/v4/anime/{anime_id}/full')
    return anime_data.json().get('data')

def clean_data(anime_data):
    """
    This function cleans the data from the JIKAN API
    """
    return {
        "mal_id": anime_data.get("mal_id"),
        "title": anime_data.get("title"),
        "anime_type": anime_data.get("type"),
        "source": anime_data.get("source"),
        "episodes": anime_data.get("episodes"),
        "status": anime_data.get("status"),
        "airing_status": anime_data.get("airing"),
        "aired_from": anime_data.get("aired", {}).get("from"),
        "aired_to": anime_data.get("aired", {}).get("to"),
        "community_score": anime_data.get("score"),
        "MAL_ranking": anime_data.get("rank"),
        "synopsis": anime_data.get("synopsis"),
        "season": anime_data.get("season"),
        "release_year": anime_data.get("year"),
        "broadcast_date": anime_data.get("broadcast", {}).get("string"),
        "broadcast_timezone": anime_data.get("broadcast", {}).get("timezone"),
        "episode_duration": anime_data.get("duration"),
        "MAL_url": anime_data.get("url"),
        "image_url": anime_data.get("images", {}).get("jpg", {}).get("image_url"),
        "studios": ", ".join([studio["name"] for studio in anime_data.get("studios", [])]),
        "genres": ", ".join([genre["name"] for genre in anime_data.get("genres", [])]),
        "themes": ", ".join([theme["name"] for theme in anime_data.get("themes", [])])
    }

if __name__ == '__main__':
    anime_data = get_data(20)
    cleaned_data = clean_data(anime_data)
    print(json.dumps(cleaned_data, indent=4))
