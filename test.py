import requests

schedule = requests.get("https://api.jikan.moe/v4/schedules").json()

print(schedule)