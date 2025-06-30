from transform import transform_weather_data
from extract import get_weather_data
from load import load_to_sqlite

def run_etl():
    get_weather_data()
    df = transform_weather_data()
    load_to_sqlite(df)

if __name__ == '__main__':
    run_etl()