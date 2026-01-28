"""
Teste pentru rutele API
"""

import pytest  # type: ignore
from src.hangman_3d import create_app


@pytest.fixture
def client():
    """Crează client test"""
    app = create_app('testing')
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test pagina index"""
    response = client.get('/')
    assert response.status_code == 200


def test_start_game_default(client):
    """Test pornire joc cu dificultate implicită"""
    response = client.post('/start_game', json={})
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['success']
    assert 'word_length' in data
    assert 'time_left' in data
    assert data['difficulty'] == 'mediu'


def test_start_game_with_difficulty(client):
    """Test pornire joc cu dificultate specifică"""
    for diff in ['usor', 'mediu', 'greu', 'expert']:
        response = client.post('/start_game', json={'difficulty': diff})
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['difficulty'] == diff


def test_guess_without_game(client):
    """Test ghicire fără joc inițiat"""
    response = client.post('/guess', json={'letter': 'A'})
    
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data


def test_guess_after_start(client):
    """Test ghicire după inițiere joc"""
    # Pornește joc
    client.post('/start_game', json={})
    
    # Ghicește
    response = client.post('/guess', json={'letter': 'A'})
    
    assert response.status_code == 200
    data = response.get_json()
    assert 'displayed_word' in data
    assert 'correct' in data


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
