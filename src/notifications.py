"""
This file contains functions for sending notifications.
For now, it simply prints the notification message.
"""

from functools import partial
from mac_notifications import client

# ✅
def send_releases_of_the_day_notification(anime_title: str, episode_number: int, link:str, streaming_service=str) -> None:
    """
    Sends a notification to the user for the release of the day.

    Args:
        anime_title (str): The title of the anime.
        episode_number (int): The episode number.
        link (str): The link to the anime.
    """

    client.create_notification(
        title=f"New Episode of {anime_title} Released!",
        subtitle=f"Episode {episode_number} is now available.",
        sound="Frog",
        text=f"Anime streaming on {streaming_service}!",
        # action_callback=partial(client.open_url, link), # TODO: Add appropriate link to the action callback
    )

# test
if __name__ == "__main__":

    send_releases_of_the_day_notification(anime_title="One Piece", episode_number=1000, link="https://www.crunchyroll.com/one-piece", streaming_service="Crunchyroll")