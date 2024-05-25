# Workshop-003

## By: Mariana Mera Gutierrez 

### Global Happiness Prediction with Apache Kafka

This project predicts the happiness score of countries using data from the 2015-2019 World Happiness Reports. The data were standardized, cleaned and combined to create a unified dataset. Linear regression and Random Forest predictive models were built. In addition, an architecture with Apache Kafka was implemented to process and store data in PostgreSQL, enabling analytics and predictions.

**Key Project Stages**

1. **Data Collection:** Obtaining global happiness reports from 2015 to 2019.

2. **Data Preprocessing:** Data cleaning and standardization to ensure consistency across years.

3. **Exploratory Data Analysis:** Initial analysis to understand distributions and relationships between variables.

4. **Feature Selection:** Identification of the most relevant features based on the correlation matrix.

5. **Model Training:** Construction and evaluation of predictive models using linear regression and Random Forest.

6. **Kafka Implementation:** Setup of a producer to send data and a consumer to receive data, predict happiness scores and store results in PostgreSQL.

7. **Model Evaluation:** Calculation of performance metrics such as MSE and R² to evaluate the accuracy of the models.

8. **Results Visualization:** Creation of maps and graphs to illustrate happiness scores and the distribution of key variables.

### Tools Technologies

- Python
- Jupiter Notebook
- Database (you choose)
- Kafka
- CSV files
- Scikit-learn library 

### Data

The data used in this project covers key indicators of well-being and happiness for different countries between 2015 and 2019. Each CSV file contains information on countries' happiness, including happiness score, GDP per capita, social support, life expectancy, freedom to make decisions, perception of corruption, and population generosity. These data allow for detailed analysis and the construction of predictive models to understand the factors that influence global happiness.

### Repository content
The structure of the repository is as follows:

- `data`: The 5 csv are found. 

- `EDA`: A folder containing the following file:
    - `EDA_csv.ipynb`: A Jupyter notebook for exploratory data analysis (EDA) on the CSV files, including data cleaning, visualization, and initial insights on the dataset.

- `Kafka`:A folder that contains the following files:

    - `main`:The main script to initiate the Kafka producer and consumer processes.
    - `producer`:Handles the extraction and transformation of CSV data, then sends the processed data to the Kafka topic.
    - `consumer`:Receives messages from the Kafka topic, makes predictions using the pre-trained model, and stores the results in the PostgreSQL database.
    - `db_connection`:Manages the connection to the PostgreSQL database, including creating tables and inserting data.
    - `transformation`:Contains functions to standardize column names, drop unnecessary columns, and handle missing data for the datasets.

- `Model`: A folder that contains the following files:
    - `random_forest_model.pkl`: It contains the Random Forest model trained to predict the happiness of countries.
    - `Prediction_Metrics.ipynb`:  This Jupyter workbook performs the analysis of model prediction metrics. It calculates metrics such as Mean Squared Error (MSE) and Coefficient of Determination (R^2) directly from data stored in the PostgreSQL database.

- `README.md`: This file you are reading now.

- `requirements.txt`: File that specifies the Python dependencies required to run the project.

- `docker-compose.yaml`: Deploy Zookeeper and Kafka services using Docker Compose. Zookeeper coordinates Kafka, a distributed messaging system. This file uses official Docker images for both services, sets network and port configuration, and defines environment variables for Kafka configuration and connection to Zookeeper. 

### Requirements
- Install Docker : [Docker Downloads](https://docs.docker.com/engine/install/)
- Install Python : [Python Downloads](https://www.python.org/downloads/)
- Install PostgreSQL : [PostgreSQL Downloads](https://www.postgresql.org/download/)

### Environment variables

To connect to the database, you will need to set some environment variables.

- `DATABASE`: Replace with the name of the database you want to use.

- `USER`: Replaces with the database user name.

- `PASSWORD`: Replaces with the password of the database user.

- `HOST`: Replace with the hostname or IP address of the PostgreSQL server.

- `PORT`: PostgreSQL server listening port.

### Run this project

1. Clone the project
~~~
git clone https://github.com/MarianaMera12/Workshop-3.git
~~~
2. Go to the project directory
~~~
cd Workshop-3
~~~
3. Create virtual environment for Python
~~~
python -m venv venv
~~~
4. Install libreries
~~~
pip install -r requirements.txt
~~~

### Run Docker 

**Requirement:** In Visual Studio Code have python and docker installed.

 - Python
   
 [![Captura-de-pantalla-2024-04-21-122151.png](https://i.postimg.cc/pLnBpp2M/Captura-de-pantalla-2024-04-21-122151.png)](https://postimg.cc/hXcmY4z2)
 - Docker
   
 [![dockervisual.png](https://i.postimg.cc/nhs3B3G5/dockervisual.png)](https://postimg.cc/SnhLp757)


5. After installing Docker, open Docker Desktop.  
[![Captura-de-pantalla-2024-04-21-124757.png](https://i.postimg.cc/nc8Fyh3w/Captura-de-pantalla-2024-04-21-124757.png)](https://postimg.cc/mhwWMBfQ)

Make sure you have your project folder ready on your system, then open Visual Studio Code and select your project folder from the 'File' > 'Open Folder' menu.
- Open the folder in visual
  
 [![estructura-w3.png](https://i.postimg.cc/G2QC2P0h/estructura-w3.png)](https://postimg.cc/47mM29Nr)

- We lift the services
  
[![wk2-parte3.png](https://i.postimg.cc/g0Zxj71f/wk2-parte3.png)](https://postimg.cc/NyQsPds4)

### If you use another code editor

In the terminal: 

~~~
docker-compose up
~~~

### Kafka 

6. Access Kafka's container.
~~~
docker exec -it kafka-test bash
~~~
7. Create a new topic called kafka-prediction.
~~~
kafka-topics --bootstrap-server kafka-test:9092 --create --topic kafka-prediction
~~~
**Note:** A terminal is required for each script. One for Consumer and one for Producer.
 
8. First run the Python script to consume messages from the topic.
~~~
python consumer.py
~~~
9. Execute the Python script to produce messages in the topic.
~~~
python producer.py
~~~

### Thank you for visiting our repository!

We hope this project will help you practice your Data Engineer skills. If you found it useful, give it a star!

Your comments and suggestions are welcome, please contribute to the project!

See you soon... 


