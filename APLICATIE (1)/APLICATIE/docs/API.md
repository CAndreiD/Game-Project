# 📡 Documentare API Hangman 3D

## Bază URL
```
http://localhost:5000
```

## Endpoints

### 1. GET `/`
Servește pagina HTML principală.

**Response:** HTML (text/html)

---

### 2. POST `/start_game`

Pornește un joc nou.

**Request:**
```json
{
    "difficulty": "mediu"
}
```

**Parametri:**
- `difficulty` (string): nivelul de dificultate
  - `"usor"` - nivel ușor (400s, 30 cuvinte)
  - `"mediu"` - nivel mediu (300s, 28 cuvinte) [default]
  - `"greu"` - nivel greu (200s, 21 cuvinte)
  - `"expert"` - nivel expert (150s, 20 cuvinte)

**Response (200):**
```json
{
    "success": true,
    "word_length": 8,
    "time_left": 300,
    "difficulty": "mediu"
}
```

**Erori (400):**
```json
{
    "error": "Dificultate invalidă"
}
```

---

### 3. POST `/guess`

Ghicește o literă.

**Request:**
```json
{
    "letter": "A"
}
```

**Parametri:**
- `letter` (string): litera de ghicit (o singură literă, case-insensitive)

**Response (200):**
```json
{
    "success": true,
    "correct": true,
    "displayed_word": "C_T",
    "wrong_guesses": 2,
    "game_over": false,
    "won": false,
    "word": null
}
```

**Response (200) - Game Over:**
```json
{
    "success": true,
    "correct": true,
    "displayed_word": "CAT",
    "wrong_guesses": 1,
    "game_over": true,
    "won": true,
    "word": "CAT"
}
```

**Parametri Response:**
- `success` (bool): operație reușită
- `correct` (bool): litera este în cuvânt
- `displayed_word` (string): cuvântul cu asteriscuri pentru litere neghetate
- `wrong_guesses` (int): numărul de greșeli
- `game_over` (bool): jocul s-a încheiat
- `won` (bool): jocul a fost câștigat
- `word` (string|null): cuvântul dacă `game_over == true`

**Erori (400):**
```json
{
    "error": "Litera a fost deja ghicită"
}
```

```json
{
    "error": "Jocul s-a încheiat"
}
```

```json
{
    "error": "Nu este inițiat niciun joc"
}
```

---

### 4. POST `/update_time`

Actualizează timp și verifica timeout.

**Request:**
```json
{
    "time_left": 250
}
```

**Parametri:**
- `time_left` (int): timp rămas în secunde

**Response (200) - Normal:**
```json
{
    "success": true,
    "time_left": 250
}
```

**Response (200) - Time Up:**
```json
{
    "time_up": true,
    "game_over": true,
    "word": "PYTHON"
}
```

---

## Exemple de Utilizare

### Flux Complet

```javascript
// 1. Pornire joc
const gameStart = await fetch('/start_game', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({difficulty: 'mediu'})
}).then(r => r.json());

console.log(`Cuvânt cu ${gameStart.word_length} litere, ${gameStart.time_left} secunde`);

// 2. Ghicire literă
const guess = await fetch('/guess', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({letter: 'A'})
}).then(r => r.json());

if (guess.correct) {
    console.log(`Corect! Cuvânt: ${guess.displayed_word}`);
} else {
    console.log(`Greșit. Greșeli: ${guess.wrong_guesses}/6`);
}

// 3. Actualizare timer
const timeUpdate = await fetch('/update_time', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({time_left: 200})
}).then(r => r.json());

if (timeUpdate.time_up) {
    console.log('TIMP SCURS! Cuvântul era: ' + timeUpdate.word);
}
```

---

## Status Codes

| Code | Înțeles |
|------|---------|
| 200 | OK - Operație reușită |
| 400 | Bad Request - Date invalide |
| 404 | Not Found - Endpoint nu există |
| 500 | Server Error - Eroare server |

---

## Rate Limiting

Momentan: **fără restricții**

(Poate fi adăugat în viitor)

---

## Versionare

API v1.0 - Stabil

---

*Documentare API Hangman 3D*
