# Developer & Contributor Guide for AniPing

Welcome to the AniPing project! This guide is intended for developers and open source contributors. It details the project structure, core modules, coding practices, and how to contribute.

---

## Table of Contents
- [Developer \& Contributor Guide for AniPing](#developer--contributor-guide-for-aniping)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Project Structure](#project-structure)
  - [Core Modules and Functions](#core-modules-and-functions)
    - [1. src/api\_functions.py](#1-srcapi_functionspy)
    - [2. src/db\_functions.py](#2-srcdb_functionspy)
    - [3. src/cli\_commands.py \& src/menu\_click.py](#3-srccli_commandspy--srcmenu_clickpy)
    - [4. src/menu\_cli.py](#4-srcmenu_clipy)
  - [Development Setup](#development-setup)
  - [Coding Conventions](#coding-conventions)
  - [Testing \& Debugging](#testing--debugging)
  - [Contribution Guidelines](#contribution-guidelines)
  - [Frequently Asked Questions](#frequently-asked-questions)
  - [Additional Resources](#additional-resources)

---

## Project Overview

AniPing is a Python CLI application for tracking anime shows, powered by the Jikan API. It uses SQLite for local storage and offers a click-driven user interface for ease of use. Notifications are sent via macOS for new episodes.

---

## Project Structure

```
AniPing/
├── aniping.py               # Main entry point
├── src/                     # Source code folder
│   ├── api_functions.py     # Functions for API interactions
│   ├── cli_commands.py      # Defines CLI commands using click
│   ├── db_functions.py      # Database CRUD functions
│   ├── menu_cli.py          # Alternative CLI menus implementation
│   └── menu_click.py        # Enhanced CLI interface using click
├── docs/                    # Documentation folder
│   ├── README.md            # User guide and project overview
│   ├── DEVELOPER_GUIDE.md   # (This file) Developer & contribution guide
│   ├── requirements.txt     # Required Python packages
│   └── LICENSE              # Project license
└── .gitignore               # Git ignore rules
```

---

## Core Modules and Functions

### 1. src/api_functions.py  
- **get_anime_info:**  
  Retrieves detailed anime information from the Jikan API.  
- **parse_and_insert_json:**  
  Parses Jikan API responses and inserts anime data into the SQLite database.

### 2. src/db_functions.py  
- Functions like `add_new_user_to_database`, `login_user`, `add_anime_to_watch_list`, and `update_user_watch_list` manage database interactions, user authentication, and list management.

### 3. src/cli_commands.py & src/menu_click.py  
- Define CLI commands using the click package.  
- Each command provides help options and invokes underlying functions from `db_functions.py` and `api_functions.py`.

### 4. src/menu_cli.py  
- Alternative implementation for CLI menus if needed, demonstrating design flexibility.

_Note: Inline comments in the source modules explain specific operations. Developers should refer to these files for detailed implementation insights._

---

## Development Setup

1. **Clone the Repository**  
   ```
   git clone https://github.com/yourusername/anime-notifications.git
   cd anime-notifications
   ```

2. **Setup a Virtual Environment**  
   Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**  
   ```
   pip install -r docs/requirements.txt
   ```

4. **Database Initialization**  
   The database is auto‑initialized on first run. For reinitialization, delete `database.db` and restart the application.

5. **Running the Application**  
   Start the project:
   ```
   python aniping.py
   ```

---

## Coding Conventions

- Follow PEP8 style guidelines.
- Include docstrings for all functions.
- Use inline comments (`# ...`) to explain non-obvious code sections.
- When modifying code in shared modules (`api_functions.py`, `db_functions.py`, etc.), include tests or descriptive logs where necessary.
- Always test new changes locally before committing.

---

## Testing & Debugging

- Leverage print statements in early development for rapid debugging.
- Consider using the Python built-in `unittest` module or pytest for automated testing.
- Run tests frequently and review outputs to ensure functionality remains intact.

---

## Contribution Guidelines

1. **Fork and Clone**  
   Fork the repository, clone locally, and create a feature branch:
   ```
   git checkout -b feature/your-feature-name
   ```

2. **Code and Document**  
   Implement features or fixes, adding comments and updating documentation as needed. Follow the coding style guidelines.

3. **Commit and Push**  
   Commit with clear messages:
   ```
   git commit -m "Describe your changes"
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request**  
   Open a Pull Request (PR) on GitHub with a detailed description of your changes, linking any related issues or discussions.

5. **Peer Review**  
   Address reviewer comments and update your PR accordingly.

---

## Frequently Asked Questions

**Q: Who can contribute?**  
A: Anyone interested in improving AniPing is welcome to contribute.

**Q: How do I report a bug?**  
A: Open an issue in the GitHub repository with a detailed description and steps to reproduce.

**Q: Where should I ask for help?**  
A: Use the GitHub Issues section for any queries or suggestions.

---

## Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [Click Documentation](https://click.palletsprojects.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Jikan API Documentation](https://jikan.moe/documentation)

---

Thank you for contributing to AniPing. Happy coding!
