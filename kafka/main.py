from kafka import KafkaProducer, KafkaConsumer
#from confluent_kafka import Producer
import pandas as pd
import joblib
from json import dumps, loads
from time import sleep, time
from db_connection import create_table, insert_data
import numpy as np

joblib_file = "../Model/random_forest_model.pkl"
model = joblib.load(joblib_file)

def kafka_producer(row):
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092'],
    )

    message = row.to_dict()
    producer.send('kafka-happiness', value=message)
    print("Message sent")

def kafka_consumer(model):
    consumer = KafkaConsumer(
        'kafka-happiness',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )

    for message in consumer:
        df = pd.json_normalize(data=message.value)
        try:
            df['Predicted_Happiness_Score'] = model.predict(df[['Economy_GDP_per_Capita', 'Social_Support', 'Health_Life_Expectancy', 'Freedom', 'Corruption', 'Generosity','Year']])
            insert_data(df.iloc[0])
            #print("Data inserted")
        except Exception as e:
            print(f"Error inserting data: {e}")