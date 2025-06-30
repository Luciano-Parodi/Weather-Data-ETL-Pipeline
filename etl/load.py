from sqlalchemy import create_engine
import os

def load_to_sqlite(df, db_path='data/clima.db', table_name='clima'):
    db_url = f"sqlite:///{db_path}"
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ Datos cargados en la tabla '{table_name}' en la base SQLite local.")


if __name__ == '__main__':
    import pandas as pd
    df = pd.DataFrame({'time': [], 'temp_celsius': []})
    load_to_sqlite(df)