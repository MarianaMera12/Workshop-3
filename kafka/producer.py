from trans import *
from sklearn.model_selection import train_test_split
import pandas as pd
from main import kafka_producer

def etl_csv():
    # Define file paths
    csv_2015 = '../data/2015.csv'
    csv_2016 = '../data/2016.csv'
    csv_2017 = '../data/2017.csv'
    csv_2018 = '../data/2018.csv'
    csv_2019 = '../data/2019.csv'

    df_2015 = pd.read_csv(csv_2015, sep=',', encoding='latin-1')
    df_2016 = pd.read_csv(csv_2016, sep=',', encoding='latin-1')
    df_2017 = pd.read_csv(csv_2017, sep=',', encoding='latin-1')
    df_2018 = pd.read_csv(csv_2018, sep=',', encoding='latin-1')
    df_2019 = pd.read_csv(csv_2019, sep=',', encoding='latin-1')

    standardize_column_1516(df_2015)
    standardize_column_1516(df_2016)
    standardize_column_17(df_2017)
    standardize_1819(df_2018)
    standardize_1819(df_2019)

    columns_to_drop_2015 = ['Region', 'Standard_Error', 'Dystopia_Residual']
    columns_to_drop_2016 = ['Region', 'Lower Confidence Interval', 'Upper Confidence Interval', 'Dystopia_Residual']
    columns_to_drop_2017 = ['Whisker_High', 'Whisker_Low', 'Dystopia_Residual']

    drop_columns(df_2015, columns_to_drop_2015)
    drop_columns(df_2016, columns_to_drop_2016)
    drop_columns(df_2017, columns_to_drop_2017)

    df_2015 = add_year_column(df_2015, 2015)
    df_2016 = add_year_column(df_2016, 2016)
    df_2017 = add_year_column(df_2017, 2017)
    df_2018 = add_year_column(df_2018, 2018)
    df_2019 = add_year_column(df_2019, 2019)


    df = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019], ignore_index=True)

    columns_to_drop = ['Country','Happiness_Rank']
    drop_columns(df,columns_to_drop)

    df = dropna_df(df)


    return df


def split_data(df):
    """
    Divide el DataFrame en conjuntos de entrenamiento y prueba para características y destino dados.

    Args:
        df (DataFrame): DataFrame que contiene los datos.

    Returns:
        DataFrame: Un DataFrame que contiene solo las filas de prueba.
    """
    # Verificar si la columna 'Year' está presente en el DataFrame
    # Seleccionar las filas de prueba
    X = df[['Economy_GDP_per_Capita', 'Social_Support', 'Health_Life_Expectancy', 'Freedom', 'Corruption', 'Generosity','Year']]
    y = df['Happiness_Score']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=59)

    # Devolver solo las filas de prueba
    return df.loc[y_test.index]


if __name__ == "__main__":
    df = etl_csv()
    df = split_data(df)
    time_between_messages = 1
    for index, row in df.iterrows():
        kafka_producer(row)
    
