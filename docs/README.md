# 📺 AniPing

> **⚠️ WARNING: This project is under active development. Use at your own risk!**

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Advanced Configuration](#advanced-configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview
AniPing is a Python CLI application for tracking your favorite anime and receiving notifications about new episodes. It uses the Jikan API to fetch anime data, stores details locally in SQLite, and leverages macOS notifications.

## Features
- 🎯 Integrates with MyAnimeList via the Jikan API
- 🔔 Sends macOS notifications for new episodes
- 📝 Provides a user-friendly click-based CLI interface
- 💾 Uses a SQLite database for local data storage

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/anime-notifications.git
cd anime-notifications
```

### 2. Install dependencies
```bash
pip install -r docs/requirements.txt
```

### 3. Database Initialization
AniPing auto‑initializes the database on first run. To reinitialize manually, delete the existing `database.db`.

## Usage

Start the application:
```bash
python aniping.py
```

Display CLI command help:
```bash
python aniping.py --help
```

CLI Commands include:
```bash
➕ add <anime_id>       - Add an anime to your watch list
➖ remove <anime_id>    - Remove an anime from your watch list
📋 list                - Display your watch list
🔄 check               - Manually check for new episodes
❌ exit                - Exit the application
```

## Advanced Configuration

- The application data is stored in `database.db` in the project root.
- Customization and environment-specific settings can be added via a configuration file or environment variables.
- For troubleshooting database issues, try deleting `database.db` and restarting the application.

## Troubleshooting

- If you encounter problems with API data, verify your internet connection.
- Use `python aniping.py --help` to review available commands and options.

## Contributing

1. 🔱 Fork the repository.
2. 🌿 Create your feature branch.
3. ✍️ Commit your changes.
4. 🚀 Push to your branch.
5. 📬 Open a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

// ...additional notes or links as needed...
