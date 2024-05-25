from transformation import *
from sklearn.model_selection import train_test_split
import pandas as pd
from main import kafka_producer

def etl_csv():

    df_2015 = pd.read_csv('../data/2015.csv')
    df_2016 = pd.read_csv('../data/2016.csv')
    df_2017 = pd.read_csv('../data/2017.csv')
    df_2018 = pd.read_csv('../data/2018.csv')
    df_2019 = pd.read_csv('../data/2019.csv')

    standardize_column_1516(df_2015)
    standardize_column_1516(df_2016)
    standardize_column_17(df_2017)
    standardize_column_1819(df_2018)
    standardize_column_1819(df_2019)

    columns_to_drop_2015 = ['Region', 'Standard_Error', 'Dystopia_Residual']
    columns_to_drop_2016 = ['Region', 'Lower Confidence Interval', 'Upper Confidence Interval', 'Dystopia_Residual']
    columns_to_drop_2017 = ['Whisker_High', 'Whisker_Low', 'Dystopia_Residual']

    drop_columns(df_2015, columns_to_drop_2015)
    drop_columns(df_2016, columns_to_drop_2016)
    drop_columns(df_2017, columns_to_drop_2017)

    df = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019], ignore_index=True)

    columns_to_drop = ['Country','Happiness_Rank']
    
    drop_columns(df,columns_to_drop)

    df = dropna_df(df)

    return df


def split_data(df):
    """
    Splits the DataFrame into training and testing sets for given features and target.

    Args:
        df (DataFrame): DataFrame containing the data.

    Returns:
        DataFrame: A DataFrame containing only the test set rows.
    """

    X = df[['Economy_GDP_per_Capita', 'Social_Support', 'Health_Life_Expectancy', 'Freedom', 'Corruption', 'Generosity']]
    y = df['Happiness_Score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=59)

    return df.loc[y_test.index]



if __name__ == "__main__":
    df = etl_csv()
    df = split_data(df)
    time_between_messages = 1
    for index, row in df.iterrows():
        kafka_producer(row)
    
