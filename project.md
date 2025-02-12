# 📺 Anime Notifications - Technical Documentation

## 🎯 Project Overview

This CLI application helps users track anime releases and receive notifications for new episodes. It uses the Jikan API for anime data and integrates with macOS notifications.

## 🏗️ System Architecture

### 🧩 Components

1. **🌐 API Interface** (api_functions.py)
   - Handles all communication with Jikan API
   - Manages rate limiting and error handling
   - Retrieves anime information and schedules

2. **💾 Database Layer** (database_operations.py)
   - SQLite3 database management
   - Stores user preferences and anime data
   - Handles data persistence

3. **🔔 Notification System** (notifications.py)
   - Manages macOS system notifications
   - Handles notification formatting and delivery

4. **🎮 Main Application** (main.py)
   - CLI interface
   - Business logic coordination
   - Schedule management

## 📚 Function Documentation

### 🌐 API Functions (api_functions.py)

#### get_anime_schedule(mal_id=None, day=None)
- 🎯 **Purpose**: Retrieves anime schedule from Jikan API
- 📥 **Parameters**:
  - mal_id (int, optional): MyAnimeList ID
  - day (str, optional): Day of the week
- 📤 **Returns**: JSON schedule data or None
- ⚠️ **Error Handling**: Manages API timeouts and invalid responses

#### get_anime_info(mal_id=int)
- 🎯 **Purpose**: Fetches detailed anime information
- 📥 **Parameters**:
  - mal_id (int): MyAnimeList ID
- 📤 **Returns**: JSON anime data or None
- ⚠️ **Error Handling**: Handles 404 and server errors

### Database Operations (database_operations.py)

#### init_database()
- 🎯 **Purpose**: Initializes SQLite database and tables
- **Tables**:
  - anime_info: Stores anime data
  - user_data: Stores user preferences
- ⚠️ **Error Handling**: Handles file system and SQL errors

## Data Structures

### Database Schema

```sql
CREATE TABLE anime_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mal_id INTEGER,
    data TEXT
);

CREATE TABLE user_data (
    user_mal_id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT UNIQUE,
    password TEXT,
    watch_list INTEGER
);
```

## 📅 Development Roadmap

### 📦 Phase 1: Core Features
- ✅ API integration
- ✅ Database initialization
- ⏳ Basic CLI interface
- ⏳ Notification system

### 🚀 Phase 2: User Features
- ⏳ Watch list management
- ⏳ User preferences
- ⏳ Schedule checking
- ⏳ Automated notifications

### ⭐ Phase 3: Advanced Features
- ⏳ Custom notification settings
- ⏳ Multiple anime tracking
- ⏳ Statistics and reporting
- ⏳ Export/Import functionality

## ✅ Implementation TODO List

1. **🔔 Notification System**
   - [ ] Implement mac_notifications integration
   - [ ] Create notification templates
   - [ ] Add notification queue management

2. **CLI Interface**
   - [ ] Design user-friendly menu system
   - [ ] Add command parsing
   - [ ] Implement help system
   - [ ] Add input validation

3. **Data Management**
   - [ ] Complete database CRUD operations
   - [ ] Add data migration capability
   - [ ] Implement backup functionality

4. **Testing**
   - [ ] Write unit tests for API functions
   - [ ] Add integration tests
   - [ ] Create test data sets

5. **Documentation**
   - [ ] Add inline code documentation
   - [ ] Create user guide
   - [ ] Document API responses

## 📝 Best Practices

1. **✨ Code Style**
   - 📏 Follow PEP 8 guidelines
   - 🏷️ Use type hints
   - 📚 Document all functions
   - 🛡️ Handle all exceptions

2. **🧪 Testing**
   - ✅ Write tests before features
   - 🔄 Mock external API calls
   - 🎯 Test edge cases
   - 📊 Maintain test coverage

3. **🔒 Security**
   - 🧹 Sanitize user input
   - 🔐 Secure API keys
   - 🛡️ Handle sensitive data properly
   - ⚖️ Implement rate limiting

## Contributing Guidelines

1. Fork the repository
2. Create feature branch
3. Follow coding standards
4. Write tests
5. Submit pull request

## 🔮 Future Enhancements

1. **🖥️ User Interface**
   - 🌐 Web interface
   - 📱 Mobile app integration
   - 💫 Rich notifications

2. **✨ Features**
   - 🔄 Multiple API support
   - 🤝 Social sharing
   - 💡 Recommendations
   - 📜 Watch history

3. **⚡ Performance**
   - 💾 Caching system
   - 📦 Batch processing
   - 🚀 Optimization