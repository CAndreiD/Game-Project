"""
Teste pentru logica jocului
"""

import pytest  # type: ignore
from src.hangman_3d.models import GameState


class TestGameState:
    """Teste pentru clasa GameState"""
    
    def test_init_default(self):
        """Test inițializare cu dificultate implicită"""
        game = GameState()
        assert game.difficulty == "mediu"
        assert game.wrong_guesses == 0
        assert game.game_over is False
        assert game.won is False
        assert len(game.guessed_letters) == 0
    
    def test_init_with_difficulty(self):
        """Test inițializare cu dificultate specifică"""
        for diff in ['usor', 'mediu', 'greu', 'expert']:
            game = GameState(diff)
            assert game.difficulty == diff
            assert game.word in __import__('src.hangman_3d.utils', fromlist=['WORDS']).WORDS[diff]
    
    def test_guess_correct_letter(self):
        """Test ghicire corectă"""
        game = GameState()
        first_letter = game.word[0]
        result = game.guess_letter(first_letter)
        
        assert result['success']
        assert result['correct']
        assert first_letter in game.guessed_letters
    
    def test_guess_wrong_letter(self):
        """Test ghicire greșită"""
        game = GameState()
        # Găsește o literă care nu e în cuvânt
        wrong_letter = None
        for letter in 'ZYXWVUTSRQPONMLKJIHGFEDCBA':
            if letter not in game.word:
                wrong_letter = letter
                break
        
        if wrong_letter:
            result = game.guess_letter(wrong_letter)
            assert result['success']
            assert not result['correct']
            assert game.wrong_guesses == 1
    
    def test_duplicate_letter(self):
        """Test ghicire literă duplicată"""
        game = GameState()
        first_letter = game.word[0]
        game.guess_letter(first_letter)
        
        result = game.guess_letter(first_letter)
        assert not result['success']
        assert 'Litera a fost deja ghicită' in result['error']
    
    def test_game_over_max_wrong(self):
        """Test Game Over la maxim greșeli"""
        game = GameState()
        # Ghicește litere greșite până la limită
        wrong_count = 0
        for letter in 'ZYXWVUTSRQPONMLKJIHGFEDCBA':
            if letter not in game.word:
                game.guess_letter(letter)
                wrong_count += 1
                if game.game_over:
                    break
        
        assert game.game_over
        assert game.wrong_guesses >= game.max_wrong


class TestGameFlow:
    """Teste pentru fluxul complet al jocului"""
    
    def test_winning_game(self):
        """Test finalizare joc câștigat"""
        game = GameState()
        # Ghicește toate literele cuvântului
        for letter in game.word:
            result = game.guess_letter(letter)
            if letter == game.word[-1]:  # Ultima literă
                assert result['won']
                assert result['game_over']
    
    def test_time_update(self):
        """Test actualizare timp"""
        game = GameState()
        result = game.update_time(100)
        
        assert result['success']
        assert game.time_left == 100
    
    def test_time_up(self):
        """Test Game Over pe timeout"""
        game = GameState()
        result = game.update_time(0)
        
        assert result['time_up']
        assert game.game_over


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
