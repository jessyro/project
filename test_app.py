# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """בדוק שהדף הבית מפנה ללוגין אם אין משתמש מחובר"""
    response = client.get('/')
    assert response.status_code == 302  # צריך להחזיר 302 (הפניה)

def test_login(client):
    """בדוק את תהליך הלוגין"""
    response = client.post('/login', data={'username': 'testuser'})
    assert response.status_code == 302  # הפניה לאחר לוגין
    assert b'Welcome to Your Calendar' in response.data

def test_logout(client):
    """בדוק את תהליך הלוג אאוט"""
    client.post('/login', data={'username': 'testuser'})
    response = client.get('/logout')
    assert response.status_code == 302  #
