import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:123456@localhost:5432/iot')

df = pd.read_csv('../data/data.csv')

df.columns = ['id', 'room_id', 'timestamp', 'temperature', 'location']

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso!")
