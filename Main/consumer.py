from main import kafka_consumer
from db_connection import create_table
import joblib

if __name__ == "__main__":
    joblib_file = "../Model/random_forest_model.pkl"
    model = joblib.load(joblib_file)
    create_table()
    kafka_consumer(model)
    