from app import app

def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Hello from GCP Cloud Run! v2.0"