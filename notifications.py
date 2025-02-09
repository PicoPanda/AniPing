"""
notifications.py
----------------
Handles sending macOS notifications using the mac_notifications client.
Refer to docs/documentation.md for overall project documentation.
"""
from functools import partial
from mac_notifications import client # type: ignore

if __name__ == "__main__":
    client.create_notification(
        title="Notification de test",
        subtitle="Ceci est un test de notification",
        # icon="/Users/jorrick/zoom.png",
        sound="Frog",
        action_button_str="Nique ta race le test",
       # action_callback=partial(join_zoom_meeting, conf_number=zoom_conf_number)
    )

# create_notification(title='Notification', subtitle=None, text=None, icon=None, sound=None, delay=timedelta(), action_button_str=None, action_callback=None, reply_button_str=None, reply_callback=None, snooze_button_str=None)
# https://jorricks.github.io/macos-notifications/user_guide/