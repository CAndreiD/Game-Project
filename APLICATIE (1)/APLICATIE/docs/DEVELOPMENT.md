# 🔧 Ghid Dezvoltare Hangman 3D

## Setup Inițial

```bash
# 1. Clone/deschide proiectul
cd hangman-3d

# 2. Instalează dependințe
pip install flask

# 3. (Optional) Instalează dev dependencies
pip install pytest pytest-cov
```

## Rulare Aplicație

### Development
```bash
python main.py
```

Server va fi disponibil la `http://localhost:5000`

### Testare
```bash
# Ruleaza toate testele
pytest tests/ -v

# Cu code coverage
pytest tests/ -v --cov=src/hangman_3d --cov-report=html
```

## Structura Directoare

```
src/
├── __init__.py
└── hangman_3d/
    ├── __init__.py (exports create_app)
    ├── app.py (Application Factory)
    ├── config.py (Configurație pe medii)
    ├── models/
    │   ├── __init__.py
    │   └── game.py (GameState - logică joc)
    ├── routes/
    │   ├── __init__.py
    │   └── game.py (API endpoints)
    └── utils/
        ├── __init__.py
        └── words.py (Bază cuvinte)
```

## Adăugare Funcții Noi

### 1. Adăugare Model Nou

Crează fișier în `src/hangman_3d/models/`:

```python
# src/hangman_3d/models/player.py
class Player:
    def __init__(self, username):
        self.username = username
        self.score = 0

# Actualizează src/hangman_3d/models/__init__.py
from .player import Player

__all__ = ["Player", "GameState"]
```

### 2. Adăugare Endpoint API

Adaugă în `src/hangman_3d/routes/game.py`:

```python
@game_bp.route('/player', methods=['POST'])
def create_player():
    """Crează jucător nou"""
    name = request.json.get('name')
    # implementare...
    return jsonify({"success": True, "player": name})
```

### 3. Adăugare Test

Crează în `tests/`:

```python
# tests/test_player.py
def test_player_creation():
    from src.hangman_3d.models import Player
    player = Player("Alice")
    assert player.username == "Alice"
    assert player.score == 0
```

## Convenții Cod

### Python
- **Style**: PEP 8
- **Docstrings**: Docstring pentru fiecare funcție/clasă
- **Type Hints**: Optionale dar recomandate
- **Imports**: Relative imports în interiorul package-ului

```python
# ✅ Bun
from hangman_3d.models import GameState
from .routes import game_bp

# ❌ Rău
from models import GameState
import app
```

### Naming
- **Clase**: PascalCase - `GameState`, `Player`
- **Funcții/Metode**: snake_case - `guess_letter()`, `create_app()`
- **Constante**: UPPER_CASE - `MAX_WRONG`, `WORDS`
- **Fișiere**: snake_case - `game.py`, `test_routes.py`

### Docstring Format
```python
def guess_letter(self, letter: str) -> Dict[str, any]:
    """
    Procesează ghicirea unei litere
    
    Args:
        letter: Litera ghicită (se convertește la majuscule)
        
    Returns:
        Dict cu rezultatul ghiciturii
    """
    pass
```

## Debugging

### Flask Debug Mode
Autommatic activat în development. Dacă nu:

```python
app.run(debug=True)
```

### Print Debugging
```python
import sys
print(f"DEBUG: {value}", file=sys.stderr)
```

### Logging (recomandat)
```python
import logging
logger = logging.getLogger(__name__)
logger.info(f"Joc inițiat: {difficulty}")
logger.error(f"Eroare: {error}")
```

## Testing Best Practices

### Unit Tests
- Testează o funcție/metodă la o dată
- Folosește fixtures pentru setup

```python
@pytest.fixture
def game():
    return GameState('mediu')

def test_guess_correct(game):
    result = game.guess_letter('P')  # PYTHON
    assert result['correct']
```

### Integration Tests
- Testează fluxul complet endpoint → backend → response

```python
def test_full_game_flow(client):
    client.post('/start_game', json={'difficulty': 'mediu'})
    result = client.post('/guess', json={'letter': 'P'})
    assert result.status_code == 200
```

### Coverage
Target: >80%

```bash
pytest --cov=src/hangman_3d --cov-report=term-missing
```

## Git Workflow

```bash
# Feature branch
git checkout -b feature/new-feature

# Commit
git add .
git commit -m "Add new feature"

# Merge
git checkout main
git merge feature/new-feature
```

## Performance Tips

1. **Caching**: Pentru WORDS (static data)
```python
from functools import lru_cache

@lru_cache(maxsize=4)
def get_words(difficulty):
    return WORDS[difficulty]
```

2. **Lazy Loading**: Inițializează Three.js doar când necesar

3. **Session Management**: Stochează game state în sesiuni pentru multiplayer

## Securitate

- ✅ Validează input pe fiecare endpoint
- ✅ Niciodată nu loga secrets
- ✅ Folosește HTTPS în producție
- ✅ Sanitizează output

## Troubleshooting

### "No module named hangman_3d"
- Asigură-te că rulezi din root: `python main.py`
- Adaugă root la PYTHONPATH: `export PYTHONPATH="${PYTHONPATH}:/path/to/project"`

### Tests nu gasesc module
- Asigură-te că ai `__init__.py` în fiecare director
- Ruleaza din root: `pytest tests/`

### Flask nu găsește templates
- Asigură-te că `templates/` este în root
- Verifică path în `app.py`: `template_folder='../../templates'`

## Resurse

- [Flask Docs](https://flask.palletsprojects.com/)
- [Pytest Docs](https://docs.pytest.org/)
- [PEP 8](https://pep8.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

*Hangman 3D Development Guide*
