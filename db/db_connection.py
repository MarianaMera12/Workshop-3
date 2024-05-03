import pandas as pd
import os
import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv
import logging

def connect_bd():

    load_dotenv()

    try:
        db_uri = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

        engine = create_engine(db_uri)

        print("Successful connection to PostgreSQL database")
        return engine
    except Exception as error:
        print("Error connecting to PostgreSQL database:", error)
        return None