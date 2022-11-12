import datetime
from fastapi.testclient import TestClient
from app.main import app

today = datetime.date.today()

client = TestClient(app)


def test_run_command():
    response = client.post("/command/", json={"command": "date"})
    assert response.status_code == 200
    assert today.strftime("%Y") in response.text
