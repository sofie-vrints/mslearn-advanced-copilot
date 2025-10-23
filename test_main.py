from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]

def test_cities_spain():
    """
    Test the /countries/Spain/cities endpoint.
    Checks that only Seville is returned for Spain.
    """
    response = client.get("/countries/Spain/cities")
    assert response.status_code == 200
    # Only Seville should be present for Spain
    assert response.json() == ["Seville"]