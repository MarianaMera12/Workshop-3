from kafka import KafkaProducer, KafkaConsumer
#from confluent_kafka import Producer
from json import dumps, loads

def kafka_producer():
    producer = KafkaProducer(
        value_serializer = lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers = ['localhost:9092'],
    )

    producer.send("kafka_lab", value={"hello": "producer"})
    print("message sent")

def kafka_consumer():
    consumer = KafkaConsumer(
        'kafka_lab',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
        )

    for m in consumer:
        print(m.value)