import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

df = pd.read_csv('C:/Users/George Kamau/Documents/Github/data-engineering-zoomcamp/01-docker-terraform/docker_hmwrk/taxi_zone_lookup.csv')

try:
    df.to_sql(name='taxi_zone_lookup', con=engine, if_exists='append', index=False)
    print("Data inserted successfully!")
except Exception as e:
    print(f"Failed to insert data: {e}")