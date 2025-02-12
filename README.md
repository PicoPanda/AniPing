# 📺 Anime Notifications

A Python CLI application that tracks your favorite anime and sends notifications when new episodes are available.

## ✨ Features

- 🎯 Track anime from MyAnimeList using the Jikan API
- 🔔 Get notifications for new episode releases
- 📝 Manage your watch list through a simple CLI interface
- 💾 SQLite database for local storage
- 🖥️ macOS notifications support

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/anime-notifications.git
cd anime-notifications
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Initialize the database:

```bash
python db_init.py
```

## 📖 Usage

4. Start the application:

```bash
python main.py
```

5. Available Commands:

```bash
➕ add <anime_id>  - Add an anime to your watch list
➖ remove <anime_id>  - Remove an anime from your watch list
📋 list  - Show your current watch list
🔄 check  - Check for new episodes manually
❌ exit  - Exit the application
```

## ⚙️ Configuration

The application stores its data in:

- 📁 `database.db`: SQLite database file
- 🛠️ Configuration is handled through the CLI interface

## 💻 Development

- 🐍 Python 3.8+
- 🌐 Uses Jikan API v4
- 🗄️ SQLite3 for data storage
- 🍎 Built for macOS notifications

## 🤝 Contributing

1. 🔱 Fork the repository
2. 🌿 Create your feature branch
3. ✍️ Commit your changes
4. 🚀 Push to the branch
5. 📬 Create a new Pull Request
