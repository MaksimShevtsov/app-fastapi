from fastapi.testclient import TestClient
from app_fastapi.main import app
from app_fastapi.settings import settings


def test_answer():
    client = TestClient(app)
    result = client.get(settings.home_url)
    assert result.status_code == 200
    assert result.json() == {'message': 'Hello, Fast api!', 'status': 'success'}
