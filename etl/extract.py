import requests
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

def get_weather_data(latitude: float = -34.6, longitude: float = -58.4) -> dict:
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    )
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    output_path = os.path.join(DATA_DIR, 'clima_raw.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Datos crudos guardados en: {output_path}")
    return data


if __name__ == '__main__':
    get_weather_data()