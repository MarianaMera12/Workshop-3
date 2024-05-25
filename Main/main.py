from kafka import KafkaProducer, KafkaConsumer
import pandas as pd
import logging
import joblib
from json import dumps, loads
from time import sleep
from db_connection import insert_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


joblib_file = "../Model/random_forest_model.pkl"
model = joblib.load(joblib_file)

def kafka_producer(row):
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092'],
    )

    message = row.to_dict()
    producer.send('kafka-prediction', value=message)
    producer.flush()  
    print("Message sent")
    
    sleep(0.2)

def kafka_consumer(model):
    consumer = KafkaConsumer(
        'kafka-prediction',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )

    for message in consumer:
        logger.info("Received message: %s", message.value)  
        df = pd.json_normalize(data=message.value)
        try:
            df['Predicted_Happiness_Score'] = model.predict(df[['Economy_GDP_per_Capita', 'Social_Support', 'Health_Life_Expectancy', 'Freedom', 'Corruption', 'Generosity']])
            insert_data(df.iloc[0])
            logger.info("Data inserted")
        except Exception as e:
            logger.error("Error inserting data: %s", e)  