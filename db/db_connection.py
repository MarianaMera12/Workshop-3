import pandas as pd
import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Definir la cadena de conexión a la base de datos como constante

Base = declarative_base()

class HappinessData(Base):
    __tablename__ = 'happiness_data'

    id = Column(Integer, primary_key=True)
    Country = Column(String)
    Happiness_Rank = Column(Integer)
    Happiness_Score = Column(Float)
    Economy_GDP_per_Capita = Column(Float)
    Social_Support = Column(Float)
    Health_Life_Expectancy = Column(Float)
    Freedom = Column(Float)
    Corruption = Column(Float)
    Generosity = Column(Float)
    Year = Column(Integer)
    Predicted_Happiness_Score = Column(Float)

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

def create_table():
    load_dotenv()

    try:
        # Utilizando db_uri definido en connect_bd()
        engine = connect_bd()
        Base.metadata.create_all(engine)
        print("Table 'happiness_data' created successfully")
    except Exception as error:
        print("Error creating table:", error)

if __name__ == "__main__":

    engine = connect_bd()
    create_table()
