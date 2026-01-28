"""
Rute pentru endpoints de joc
"""

from typing import Optional
from flask import Blueprint, render_template, jsonify, request
from ..models import GameState

game_bp = Blueprint('game', __name__)

# Starea globală a jocului (în producție, ar trebui să folosească sesiuni)
game_state: Optional[GameState] = None


@game_bp.route('/')
def index():
    """Servește pagina principală"""
    return render_template('index.html')


@game_bp.route('/start_game', methods=['POST'])
def start_game():
    """
    Pornește un joc nou
    
    Request JSON:
        - difficulty: str (usor, mediu, greu, expert)
        
    Response:
        - success: bool
        - word_length: int
        - time_left: int
        - difficulty: str
    """
    global game_state
    
    difficulty = request.json.get('difficulty', 'mediu') if request.json else 'mediu'
    
    # Validare dificultate
    if difficulty not in ['usor', 'mediu', 'greu', 'expert']:
        difficulty = 'mediu'
    
    game_state = GameState(difficulty)
    
    return jsonify({
        "success": True,
        "word_length": len(game_state.word),
        "time_left": game_state.time_left,
        "difficulty": difficulty
    })


@game_bp.route('/guess', methods=['POST'])
def guess_letter():
    """
    Ghicește o literă
    
    Request JSON:
        - letter: str (o singură literă)
        
    Response:
        - correct: bool
        - displayed_word: str
        - wrong_guesses: int
        - game_over: bool
        - won: bool
        - word: str (doar dacă game_over)
    """
    global game_state
    
    if game_state is None:
        return jsonify({"error": "Nu este inițiat niciun joc"}), 400
    
    letter = request.json.get('letter', '') if request.json else ''
    
    if not letter:
        return jsonify({"error": "Nicio literă furnizată"}), 400
    
    result = game_state.guess_letter(letter)
    
    if not result.get('success'):
        return jsonify(result), 400
    
    return jsonify(result)


@game_bp.route('/update_time', methods=['POST'])
def update_time():
    """
    Actualizează timp rămas
    
    Request JSON:
        - time_left: int (secunde)
        
    Response:
        - success: bool
        - time_left: int (sau time_up: bool dacă timeout)
    """
    global game_state
    
    if game_state is None:
        return jsonify({"error": "Nu este inițiat niciun joc"}), 400
    
    time_left = request.json.get('time_left', 0) if request.json else 0
    result = game_state.update_time(time_left)
    
    return jsonify(result)
