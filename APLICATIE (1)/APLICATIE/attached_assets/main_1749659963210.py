
from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Lista de cuvinte pentru joc pe nivele
WORDS = {
    "usor": [
        "CAT", "DOG", "SUN", "CAR", "RED", "BOY", "RUN", "EAT", "BIG", "HOT",
        "ICE", "TREE", "BOOK", "FISH", "BIRD", "LOVE", "BLUE", "FAST", "COLD", "WARM",
        "HAT", "BED", "CUP", "BAG", "TOY", "PEN", "EGG", "BOX", "KEY", "MAN"
    ],
    "mediu": [
        "PYTHON", "COMPUTER", "KEYBOARD", "MONITOR", "INTERNET", "WEBSITE", 
        "DATABASE", "FUNCTION", "VARIABLE", "OBJECT", "SCHOOL", "FRIEND", 
        "FAMILY", "HAPPY", "STRONG", "BRIGHT", "QUIET", "NATURE", "MOUNTAIN", "OCEAN",
        "GUITAR", "PLANET", "CASTLE", "DRAGON", "FOREST", "BRIDGE", "ROCKET", "GARDEN"
    ],
    "greu": [
        "JAVASCRIPT", "PROGRAMMING", "ALGORITHM", "FRAMEWORK", "DEVELOPMENT",
        "ARCHITECTURE", "OPTIMIZATION", "DEPLOYMENT", "CONFIGURATION", "AUTHENTICATION",
        "ENCRYPTION", "ABSTRACTION", "INHERITANCE", "POLYMORPHISM", "ENCAPSULATION",
        "ADVENTURE", "KNOWLEDGE", "CHALLENGE", "DISCOVERY", "UNIVERSE", "CREATIVE"
    ],
    "expert": [
        "CRYPTOCURRENCY", "MICROSERVICES", "CONTAINERIZATION", "ORCHESTRATION",
        "VIRTUALIZATION", "PARALLELIZATION", "SYNCHRONIZATION", "MULTITHREADING",
        "ASYNCHRONOUS", "RESPONSIBILITY", "ACCOUNTABILITY", "SUSTAINABILITY",
        "IMPLEMENTATION", "TRANSFORMATION", "REVOLUTIONARY", "EXTRAORDINARY",
        "CONSTITUTIONAL", "INTERDISCIPLINARY", "INTERNATIONALLY", "CHARACTERIZATION"
    ]
}

# Starea jocului
game_state = {
    "word": "",
    "guessed_letters": [],
    "wrong_guesses": 0,
    "max_wrong": 6,
    "game_over": False,
    "won": False,
    "time_left": 300,
    "difficulty": "mediu"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    global game_state
    difficulty = request.json.get('difficulty', 'mediu')
    
    # Timp diferit pe nivel
    time_limits = {"usor": 400, "mediu": 300, "greu": 200, "expert": 150}
    
    game_state = {
        "word": random.choice(WORDS[difficulty]),
        "guessed_letters": [],
        "wrong_guesses": 0,
        "max_wrong": 6,
        "game_over": False,
        "won": False,
        "time_left": time_limits[difficulty],
        "difficulty": difficulty
    }
    return jsonify({
        "success": True,
        "word_length": len(game_state["word"]),
        "time_left": game_state["time_left"],
        "difficulty": difficulty
    })

@app.route('/guess', methods=['POST'])
def guess_letter():
    global game_state
    
    if game_state["game_over"]:
        return jsonify({"error": "Game is over"})
    
    letter = request.json.get('letter', '').upper()
    
    if letter in game_state["guessed_letters"]:
        return jsonify({"error": "Letter already guessed"})
    
    game_state["guessed_letters"].append(letter)
    
    if letter in game_state["word"]:
        # Verifică dacă a câștigat
        if all(l in game_state["guessed_letters"] for l in game_state["word"]):
            game_state["won"] = True
            game_state["game_over"] = True
    else:
        game_state["wrong_guesses"] += 1
        if game_state["wrong_guesses"] >= game_state["max_wrong"]:
            game_state["game_over"] = True
    
    # Creează cuvântul afișat
    displayed_word = ''.join(
        letter if letter in game_state["guessed_letters"] else '_'
        for letter in game_state["word"]
    )
    
    return jsonify({
        "correct": letter in game_state["word"],
        "displayed_word": displayed_word,
        "wrong_guesses": game_state["wrong_guesses"],
        "game_over": game_state["game_over"],
        "won": game_state["won"],
        "word": game_state["word"] if game_state["game_over"] else None
    })

@app.route('/update_time', methods=['POST'])
def update_time():
    global game_state
    game_state["time_left"] = request.json.get('time_left', 0)
    
    if game_state["time_left"] <= 0 and not game_state["game_over"]:
        game_state["game_over"] = True
        return jsonify({
            "time_up": True,
            "game_over": True,
            "word": game_state["word"]
        })
    
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
