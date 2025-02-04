import pandas as pd
from sqlalchemy import create_engine
from time import time

engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

df_iter = pd.read_csv('C:/Users/George Kamau/Documents/Github/data-engineering-zoomcamp/01-docker-terraform/docker_hmwrk/green_tripdata_2019-10.csv', iterator=True, chunksize=100000)

df = next(df_iter)

# Convert datetime columns to datetime objects
df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

# Create the table with the first chunk
df.head(0).to_sql(name='green_tripdata_2019-10', con=engine, if_exists='replace', index=False)
df.to_sql(name='green_tripdata_2019-10', con=engine, if_exists='append', index=False)


while True: 
    t_start = time()

    try:
        df = next(df_iter)
    except StopIteration:
        break

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    
    df.to_sql(name='green_tripdata_2019-10', con=engine, if_exists='append', index=False)

    t_end = time()

    print('inserted another chunk, took %.3f second' % (t_end - t_start))