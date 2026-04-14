from app import app

def test_submit_valid_city(monkeypatch):
    client = app.test_client()


    monkeypatch.setattr(
        "APITesting.get_weather",
        lambda city: {
            "tempNow": 70,
            "feels_like": 68,
            "temp_max": 75,
            "temp_min": 60,
            "condition": 1
        }
    )

    response = client.post("/submit", data={"city": "Phoenix"})

    assert response.status_code == 200
    assert b"Phoenix" in response.data
    assert b'data-code="1"' in response.data


def test_submit_empty_city():
    client = app.test_client()

    response = client.post("/submit", data={"city": ""})

    assert response.status_code == 200
    assert b"Please enter a city." in response.data


def test_submit_invalid_city(monkeypatch):
    client = app.test_client()


    monkeypatch.setattr("app.error_check", lambda c: "Invalid city")


    response = client.post("/submit", data={"city": "1234"})

    assert response.status_code == 200
    assert b"Invalid city" in response.data

