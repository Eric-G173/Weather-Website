from app import app
from API_Function import reverse_geocode
def test_submit_valid_city(monkeypatch):
    client = app.test_client()


    monkeypatch.setattr(
        "API_Function.get_weather",
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
    assert b'data-code="' in response.data



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

def test_reverse_geocode(monkeypatch):
    def fake_get(url, params=None, headers=None):
        class FakeResponse:
            def json(self):
                return {
                    "address": {"city": "Phoenix"}
                }
        return FakeResponse()

    monkeypatch.setattr("API_Function.requests.get", fake_get)

    city = reverse_geocode(33.3, -112.0)
    assert city == "Phoenix"
