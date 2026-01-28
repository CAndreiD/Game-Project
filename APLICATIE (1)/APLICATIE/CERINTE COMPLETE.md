# Hangman 3D

## Overview

Hangman 3D is a modern web-based implementation of the classic "Hangman" word-guessing game featuring 3D rendering with Three.js, procedural audio effects, a responsive interface, AND an integrated data collection pipeline that fetches, processes, exports, and visualizes data from external APIs.

## Status: ✅ COMPLETE

All requirements have been implemented and tested:
- Core game with 4 difficulty levels ✅
- 3D rendering with Three.js ✅
- REST API data pipeline (collect → process → CSV → PNG) ✅
- Full test coverage with pytest ✅
- Comprehensive documentation (GDPR, Security, Licenses) ✅
- Structured src/ layout with classes ✅
- Poetry dependency management ✅

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Structure (Python/Flask)
- **src Layout Pattern**: All source code under `src/hangman_3d/` following Python packaging best practices
- **Application Factory**: Flask `create_app()` pattern for flexible configuration
- **Blueprint Architecture**: Routes organized using Flask Blueprints
- **Configuration Management**: Environment-specific configs (DevelopmentConfig, TestingConfig, ProductionConfig)

### Data Pipeline Architecture
The application includes a complete ETL pipeline:

1. **APIClient** (`api_client.py`)
   - Fetches data from JSONPlaceholder API (https://jsonplaceholder.typicode.com)
   - Methods: fetch_posts(), fetch_users(), fetch_comments()
   - Handles HTTPS + error handling

2. **DataProcessor** (`data_processor.py`)
   - Processes raw API data
   - Methods: filter_by_field(), extract_fields(), aggregate_by_field(), count_by_field(), get_statistics()

3. **CSVExporter** (`csv_exporter.py`)
   - Exports data to CSV format
   - Methods: export_data(), export_aggregated()
   - Output: `output/*.csv`

4. **DataVisualizer** (`visualizer.py`)
   - Creates PNG charts using matplotlib
   - Methods: create_bar_chart(), create_pie_chart(), create_line_chart(), create_histogram()
   - Output: `output/*.png`

5. **DataPipeline** (`data_pipeline.py`)
   - Orchestrates the full flow: fetch → process → export CSV → create PNG
   - Run via: `GET /api/data/pipeline` endpoint

### Module Organization
```
src/hangman_3d/
├── models/game.py           - GameState class
├── routes/game.py           - API endpoints
├── utils/words.py           - Word database
├── app.py                   - Flask factory + API routes
├── config.py                - Configuration
├── logger.py                - Logging setup
├── api_client.py            - REST API client
├── data_processor.py        - Data processing
├── csv_exporter.py          - CSV export
├── visualizer.py            - Chart generation
├── data_pipeline.py         - Pipeline orchestration
└── __init__.py              - Package initialization
```

### Game State Management
- `GameState` class encapsulates game logic
- Methods: guess_letter(), update_time(), get_display_word()
- Manages: word selection, guessed letters, wrong count, win/lose conditions
- Session-based management (can be improved with server-side sessions)

### Frontend Architecture
- **Three.js r128**: 3D rendering of hangman figure
- **Web Audio API**: Procedural sound generation
- **Single Page Application**: All UI in `templates/index.html`

## External Dependencies

### Python Packages (Poetry-managed)
- **Flask 3.1+**: Web framework
- **Requests 2.31+**: HTTP client for API calls
- **Pandas 2.0+**: Data manipulation
- **Matplotlib 3.8+**: Data visualization
- **Pytest 7.4+**: Testing framework
- **Pytest-cov 4.1+**: Code coverage

### Frontend Libraries (CDN)
- **Three.js r128**: 3D graphics via CDNjs

### External APIs
- **JSONPlaceholder**: Demo public API for data pipeline testing

## Data Files

### Generated on Pipeline Execution
- `output/posts_data.csv` - Post metadata from API
- `output/users_data.csv` - User data from API
- `output/posts_by_user.png` - Bar chart visualization
- `output/users_distribution.png` - Pie chart visualization

### Application Logs
- `logs/app_*.log` - Timestamped application logs with INFO/ERROR/DEBUG levels

## Documentation

### Code Documentation
- `docs/ARCHITECTURE.md` - System design and module relationships
- `docs/API.md` - API endpoint specifications
- `docs/DEVELOPMENT.md` - Setup and contribution guidelines
- `docs/REQUIREMENTS_CHECKLIST.md` - Feature checklist

### Compliance & Security
- `docs/GDPR.md` - Data privacy policy & GDPR compliance
- `docs/SECURITY.md` - Security measures, threats, production recommendations
- `LICENSES.txt` - License audit for all dependencies
- `README.md` - Main documentation with diagrams

## How to Run

### Development
```bash
# Install dependencies
poetry install

# Run Flask server
poetry run python main.py

# Run tests
poetry run pytest tests/ -v --cov=src/hangman_3d

# Access game at http://localhost:5000
```

### Data Pipeline
```bash
# Option 1: Via API endpoint
curl http://localhost:5000/api/data/pipeline

# Generated files:
# - output/posts_data.csv
# - output/users_data.csv
# - output/posts_by_user.png
# - output/users_distribution.png
```

## Testing

- **Unit Tests**: `tests/test_game.py` - GameState class (9 tests)
- **Integration Tests**: `tests/test_routes.py` - API endpoints (5 tests)
- **Coverage**: Configured in pyproject.toml with pytest-cov

## Security & Privacy

✅ **No tracking, no cookies, no analytics**
✅ **GDPR compliant** - See docs/GDPR.md
✅ **Secure by design** - See docs/SECURITY.md
✅ **All licenses documented** - See LICENSES.txt

## Recent Changes (Latest Session)

1. **Data Pipeline Implementation**
   - Added APIClient for REST API integration
   - Added DataProcessor for data transformation
   - Added CSVExporter for CSV generation
   - Added DataVisualizer for PNG chart creation
   - Added DataPipeline orchestrator
   - Added Logger module with file + console output

2. **API Routes**
   - GET `/api/data/pipeline` - Execute full data pipeline
   - GET `/api/data/status` - Check pipeline status

3. **Documentation**
   - Created docs/GDPR.md - Data privacy and user rights
   - Created docs/SECURITY.md - Security measures and recommendations
   - Created LICENSES.txt - License audit of all dependencies
   - Updated replit.md - Complete architecture overview

4. **Dependencies**
   - requests 2.31+ for REST API calls
   - pandas 2.0+ for data processing
   - matplotlib 3.8+ for visualization
   - All managed via Poetry in pyproject.toml

## File Structure

```
hangman-3d/
├── src/hangman_3d/               # Main package
│   ├── models/game.py            # GameState
│   ├── routes/game.py            # Game API
│   ├── utils/words.py            # Word DB
│   ├── api_client.py             # REST client
│   ├── data_processor.py         # Data processing
│   ├── csv_exporter.py           # CSV export
│   ├── visualizer.py             # Chart generation
│   ├── data_pipeline.py          # Pipeline
│   ├── logger.py                 # Logging
│   ├── app.py                    # Flask factory
│   ├── config.py                 # Configuration
│   └── __init__.py               # Package init
├── templates/index.html          # 3D frontend
├── tests/                        # Pytest tests
├── docs/                         # Documentation
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── DEVELOPMENT.md
│   ├── GDPR.md                   # NEW
│   ├── SECURITY.md               # NEW
│   ├── architecture-diagram.svg
│   └── process-flow-diagram.svg
├── output/                       # Generated data
├── logs/                         # Application logs
├── main.py                       # Entry point
├── pyproject.toml                # Poetry config
├── poetry.lock                   # Dependency lock
├── README.md                     # Full docs with diagrams
├── LICENSES.txt                  # License audit
├── LICENSE                       # MIT License
└── .gitignore                    # Git config
```

## Next Steps (Post-MVP)

1. **Session Management**: Replace global game state with server-side sessions
2. **Database**: Add PostgreSQL for persistent data storage
3. **User Accounts**: Implement authentication and user profiles
4. **Advanced Analytics**: Store game statistics and leaderboards
5. **Production Deployment**: Docker, Kubernetes, cloud deployment
6. **Security Hardening**: Rate limiting, CSRF tokens, Security headers
7. **Accessibility**: WCAG 2.1 AA compliance for visually impaired users
