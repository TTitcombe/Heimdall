"""
Call carbon intensity APIs
"""
import requests


def get_carbon_intensity() -> float:
    response = requests.get("https://FAKEAPI.carbon/")

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching intensity: {response.json()}")
    else:
        return response.json()["intensity"]
