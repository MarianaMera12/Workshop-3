import pandas as pd
import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import numpy as np


# Definir la cadena de conexión a la base de datos como constante

Base = declarative_base()

class HappinessData(Base):
    __tablename__ = 'happiness_table'

    id = Column(Integer, primary_key=True)
    Economy_GDP_per_Capita = Column(Float)
    Social_Support = Column(Float)
    Health_Life_Expectancy = Column(Float)
    Freedom = Column(Float)
    Corruption = Column(Float)
    Generosity = Column(Float)
    Year = Column(Integer)
    Happiness_Score = Column(Float)
    Predicted_Happiness_Score = Column(Float)

def connect_bd():
    load_dotenv()

    try:
        db_uri = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        engine = create_engine(db_uri)
        return engine
    except Exception as error:
        # Mejor manejo de excepciones
        logging.error("Error connecting to PostgreSQL database: %s", error)
        return None

def create_table():
    load_dotenv()

    try:
        engine = connect_bd()
        Base.metadata.create_all(engine)
        return True
    except Exception as error:
        logging.error("Error creating table: %s", error)
        return False

def insert_data(data):
    try:
        engine = connect_bd()
        Session = sessionmaker(bind=engine)
        session = Session()

        # Crear una instancia de HappinessData con los datos proporcionados
        new_data = HappinessData(
            Economy_GDP_per_Capita=data['Economy_GDP_per_Capita'],
            Social_Support=data['Social_Support'],
            Health_Life_Expectancy=data['Health_Life_Expectancy'],
            Freedom=data['Freedom'],
            Corruption=data['Corruption'],
            Generosity=data['Generosity'],
            Year=data['Year'],
            Happiness_Score=data['Happiness_Score'],
            Predicted_Happiness_Score=data['Predicted_Happiness_Score']
        )

        session.add(new_data)
        session.commit()
        session.close()
        logging.info("Data inserted successfully.")
        return True
    except Exception as error:
        logging.error("Error inserting data: %s", error)
        logging.error("Data that caused the error: %s", data)
        return False


    
if __name__ == "__main__":
    # Manejo de resultados de la creación de la tabla
    if create_table():
        print("Table 'happiness_table' created successfully")
    else:
        print("Failed to create table 'happiness_table'")
    
