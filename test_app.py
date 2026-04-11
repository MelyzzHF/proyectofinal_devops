import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Prueba que el servidor responda y contenga el texto Hola Mundo"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Hola Mundo' in rv.data
