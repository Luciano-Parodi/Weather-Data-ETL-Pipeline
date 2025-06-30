import pandas as pd
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def transform_weather_data(input_file: str = None) -> pd.DataFrame:
    input_path = (
        input_file
        or os.path.join(DATA_DIR, 'clima_raw.json')
    )
    with open(input_path, 'r', encoding='utf-8') as f:
        raw = json.load(f)

    df = pd.DataFrame(raw['hourly'])
    df['time'] = pd.to_datetime(df['time'])
    df.rename(columns={'temperature_2m': 'temp_celsius'}, inplace=True)

    print(f"Transformación completada: {len(df)} registros procesados.")
    return df

if __name__ == '__main__':
    import sys
    df = transform_weather_data()
    print(df.head())