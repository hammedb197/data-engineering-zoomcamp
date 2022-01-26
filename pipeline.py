import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

import argparse


def ingest(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database = params.db
    db_table = params.table

    print('hey)')
    # output = params.output



    # engine = create_engine("database_type://user:password@host_url/db_name")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

    # engine.connect()

    df = pd.read_csv('yellow_tripdata_2021-01.csv')
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    print('data schema', pd.io.sql.get_schema(df, name=db_table))

    df.to_sql(name= db_table, con=engine, if_exists='append')
    print('data saved')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='in gest csv to postgres')
    parser.add_argument("--user", help="user for postgres")
    parser.add_argument("--password", help="password for postgres")
    parser.add_argument("--host", help="host for postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--db",  help="database for postgres")
    parser.add_argument("--table", help="table for postgres")
    # parser.add_argument("output",  help="output for postgres")
    args = parser.parse_args()
    print(ingest(args))


