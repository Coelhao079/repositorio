import json
import urllib.request
import pytest

def test_api_integration_flow():
    url = "https://api.adviceslip.com/advice"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            assert response.status == 200
            content = response.read().decode()
            data = json.loads(content)
            assert "slip" in data
            assert "advice" in data["slip"]
            assert isinstance(data["slip"]["advice"], str)
    except Exception as e:
        pytest.fail(f"Erro na integração: {e}")
