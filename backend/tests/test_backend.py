from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def is_legit(url: str):
    response = client.post("/v1/analyze", json={"url": url})
    result = response.json()
    return result["is_legit"]


def test_healthcheck():
    assert client.get("/").status_code == 200


def test_response():
    response = client.post("/v1/analyze", json={"url": "https://www.google.com"})
    assert response.status_code == 200


def test_legit_urls():
    assert is_legit("https://www.google.com")
    assert is_legit("https://www.facebook.com")
    assert is_legit("https://www.github.com")
    assert is_legit("https://www.voicefmradio.co.uk")


def test_phishing_urls():
    assert not is_legit("http://www.kuradox92.lima-city.de")
    assert not is_legit("http://www.f0519141.xsph.ru")
    assert not is_legit("https://bancolombia.com1home0892.repl.co/?2")
