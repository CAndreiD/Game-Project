# 🏗️ Arhitectura Hangman 3D

## Imagine Generală

Hangman 3D este o aplicație web modernă care implementează jocul clasic "Spânzurătoarea" cu rendering 3D și efecte vizuale avansate.

## Structura Proiectului (src Layout)

```
hangman-3d/
├── src/
│   ├── __init__.py
│   └── hangman_3d/
│       ├── __init__.py (create_app factory)
│       ├── app.py (creare aplicație Flask)
│       ├── config.py (configurare medii)
│       ├── models/
│       │   ├── __init__.py
│       │   └── game.py (logica jocului - GameState)
│       ├── routes/
│       │   ├── __init__.py
│       │   └── game.py (endpoints API)
│       └── utils/
│           ├── __init__.py
│           └── words.py (bază de cuvinte)
├── templates/
│   └── index.html (interfață 3D cu Three.js)
├── tests/
│   ├── __init__.py
│   ├── test_game.py (teste logică joc)
│   └── test_routes.py (teste API)
├── docs/
│   ├── ARCHITECTURE.md (acest fișier)
│   ├── API.md (documentare endpoints)
│   └── DEVELOPMENT.md (ghid dezvoltare)
├── main.py (punct de intrare)
├── pyproject.toml (configurare proiect)
└── .gitignore
```

## Componente Principale

### 1. **Backend (src/hangman_3d/)**

#### `app.py` - Application Factory
- Crează și configurează aplicația Flask
- Înregistrează blueprint-uri
- Setează error handlers

#### `config.py` - Configurație
- Clase de configurare pentru development, testing, production
- Variabile de mediu

#### `models/game.py` - GameState
- **Atribute principale:**
  - `word`: cuvântul de ghicit
  - `guessed_letters`: literele ghicite
  - `wrong_guesses`: numărul de greșeli
  - `game_over`: flag pentru sfârşit
  - `time_left`: timp rămas

- **Metode principale:**
  - `guess_letter(letter)`: procesează o ghicire
  - `update_time(time_left)`: actualizează cronometru
  - `get_display_word()`: cuvântul cu asteriscuri

#### `routes/game.py` - Endpoints API
- `POST /start_game` - pornire joc
- `POST /guess` - ghicire literă
- `POST /update_time` - actualizare cronometru
- `GET /` - servire HTML

#### `utils/words.py` - Bază de Date
- Cuvinte pe 4 nivele de dificultate
- 120+ cuvinte total

### 2. **Frontend (templates/index.html)**

- **Three.js 3D Engine**: rendering spânzurătoarei
- **Web Audio API**: efecte sonore și muzică
- **Interfață Interactivă**: butoane și controale tastatură
- **Animații CSS3**: efecte vizuale

## Flux de Date

```
Frontend                    Backend
   ↓                          ↓
[User Input]  →  POST /start_game  →  [GameState created]
     ↑                         ↓
     ← [Response JSON] ←  [get word_length]
     
[User Input]  →  POST /guess  →  [GameState.guess_letter()]
     ↑                         ↓
     ← [Response JSON] ←  [check correct/wrong]

[Timer]  →  POST /update_time  →  [GameState.update_time()]
     ↑                         ↓
     ← [Response JSON] ←  [check timeout]
```

## Nivele de Dificultate

| Nivel | Timp | Cuvinte | Lungime |
|-------|------|---------|---------|
| Ușor | 400s | 30 | 3-4 lit |
| Mediu | 300s | 28 | 5-8 lit |
| Greu | 200s | 21 | 9-13 lit |
| Expert | 150s | 20 | 14+ lit |

## Flux de Joc

1. **Inițiere**
   - User selectează dificultate
   - POST `/start_game` cu nivelul
   - Server crează GameState
   - Frontend inițializează timer și Three.js

2. **Gameplay**
   - User ghicește litere (click/tastă)
   - POST `/guess` cu litera
   - Server procesează, returnează stare
   - Frontend actualizează display și 3D

3. **Cronometru**
   - Frontend decrementează timer
   - POST `/update_time` periodic
   - Server verifica timeout
   - Game over dacă timp = 0

4. **Sfârşit**
   - Win: toate literele ghicite
   - Loss: 6 greșeli sau timeout
   - Frontend afișează overlay cu rezultat

## Dependențe

### Production
- **Flask >= 3.1.1**: framework web Python

### Development
- **pytest >= 7.4.0**: testare
- **pytest-cov >= 4.1.0**: coverage

### Frontend (CDN)
- **Three.js r128**: rendering 3D
- **Web Audio API**: nativ în browser

## Strategia de Testare

### Unit Tests (`test_game.py`)
- Testează logica GameState
- Validează ghiciri, timeout, game over

### Integration Tests (`test_routes.py`)
- Testează endpoints API
- Validează fluxul complet

### Coverage
Target: >80% code coverage

## Instalare și Rulare

```bash
# Instalare dependințe
pip install flask

# Dev
python main.py

# Testare
pytest tests/ -v --cov=src/hangman_3d
```

## Securitate

- ✅ Input validation pe cuvintele din WORDS
- ✅ Nicio expunere de secrets
- ✅ Error messages standard

## Extensibilitate

Proiectul este ușor extendibil pentru:
- Multiplayer (cu sesiuni)
- Baza de date (cu SQLAlchemy)
- Leaderboard
- Categorii tematice
- Achievements

---
*Hangman 3D - Arhitectură modulară și scalabilă*
