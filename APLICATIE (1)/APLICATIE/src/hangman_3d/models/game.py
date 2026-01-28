"""
Model pentru starea jocului și logica de ghicire
"""

import random
from typing import Dict, List, Any
from ..utils import WORDS


class GameState:
    """
    Gestiunea stării jocului Hangman
    
    Atribute:
        word: Cuvântul de ghicit
        guessed_letters: Lista literelor ghicite
        wrong_guesses: Numărul de greșeli
        max_wrong: Numărul maxim de greșeli permise
        game_over: Flag pentru sfârșit joc
        won: Flag pentru victorie
        time_left: Timp rămas în secunde
        difficulty: Nivel de dificultate
    """
    
    def __init__(self, difficulty: str = "mediu"):
        """
        Inițializează o nouă stare de joc
        
        Args:
            difficulty: Nivelul de dificultate (usor, mediu, greu, expert)
        """
        self.difficulty = difficulty
        self.word = random.choice(WORDS[difficulty])
        self.guessed_letters: List[str] = []
        self.wrong_guesses = 0
        self.max_wrong = 6
        self.game_over = False
        self.won = False
        
        # Timp diferit pentru fiecare nivel
        time_limits = {"usor": 400, "mediu": 300, "greu": 200, "expert": 150}
        self.time_left = time_limits[difficulty]
    
    def guess_letter(self, letter: str) -> Dict[str, Any]:
        """
        Procesează ghicirea unei litere
        
        Args:
            letter: Litera ghicită (se convertește la majuscule)
            
        Returns:
            Dict cu rezultatul ghiciturii
        """
        letter = letter.upper()
        
        # Validări
        if self.game_over:
            return {
                "success": False,
                "error": "Jocul s-a încheiat"
            }
        
        if letter in self.guessed_letters:
            return {
                "success": False,
                "error": "Litera a fost deja ghicită"
            }
        
        # Adaugă litera
        self.guessed_letters.append(letter)
        
        # Verifică dacă este corectă
        is_correct = letter in self.word
        
        if is_correct:
            # Verifică dacă a câștigat
            if all(l in self.guessed_letters for l in self.word):
                self.won = True
                self.game_over = True
        else:
            # Greșeală
            self.wrong_guesses += 1
            if self.wrong_guesses >= self.max_wrong:
                self.game_over = True
        
        return self._get_response()
    
    def _get_response(self) -> Dict[str, Any]:
        """Construiește răspunsul pentru o ghicire"""
        displayed_word = ''.join(
            letter if letter in self.guessed_letters else '_'
            for letter in self.word
        )
        
        return {
            "success": True,
            "correct": len(self.guessed_letters) > 0 and self.guessed_letters[-1] in self.word,
            "displayed_word": displayed_word,
            "wrong_guesses": self.wrong_guesses,
            "game_over": self.game_over,
            "won": self.won,
            "word": self.word if self.game_over else None
        }
    
    def update_time(self, time_left: int) -> Dict[str, Any]:
        """
        Actualizează timp și verifică dacă s-a terminat
        
        Args:
            time_left: Timp rămas în secunde
            
        Returns:
            Dict cu status-ul
        """
        self.time_left = time_left
        
        if self.time_left <= 0 and not self.game_over:
            self.game_over = True
            return {
                "time_up": True,
                "game_over": True,
                "word": self.word
            }
        
        return {
            "success": True,
            "time_left": self.time_left
        }
    
    def get_display_word(self) -> str:
        """Returnează cuvântul cu literele ascunse"""
        return ''.join(
            letter if letter in self.guessed_letters else '_'
            for letter in self.word
        )
