
def standardize_column_1516(df):
    """
    Standardizes column names for 2015 and 2016 DataFrames.
    """
    new_column_names = {
        'Country': 'Country',
        'Region': 'Region',
        'Happiness Rank': 'Happiness_Rank',
        'Happiness Score': 'Happiness_Score',
        'Standard Error': 'Standard_Error',
        'Economy (GDP per Capita)': 'Economy_GDP_per_Capita',
        'Family': 'Social_Support',
        'Health (Life Expectancy)': 'Health_Life_Expectancy',
        'Freedom': 'Freedom',
        'Trust (Government Corruption)': 'Corruption',
        'Generosity': 'Generosity',
        'Dystopia Residual': 'Dystopia_Residual'
    }

    df.rename(columns=new_column_names, inplace=True)


def standardize_column_17(df):
    """
    Standardizes column names for 2017 DataFrame.
    """
    new_column_names = {
        'Country': 'Country',
        'Happiness.Rank': 'Happiness_Rank',
        'Happiness.Score': 'Happiness_Score',
        'Whisker.high': 'Whisker_High',
        'Whisker.low': 'Whisker_Low',
        'Economy..GDP.per.Capita.': 'Economy_GDP_per_Capita',
        'Family': 'Social_Support',
        'Health..Life.Expectancy.': 'Health_Life_Expectancy',
        'Freedom': 'Freedom',
        'Generosity': 'Generosity',
        'Trust..Government.Corruption.': 'Corruption',
        'Dystopia.Residual': 'Dystopia_Residual'
    }

    df.rename(columns=new_column_names, inplace=True)


def standardize_column_1819(df):
    """
    Standardizes column names for 2018 and 2019 DataFrames.
    """
    new_column_names = {
        'Overall rank': 'Happiness_Rank',
        'Country or region': 'Country',
        'Score': 'Happiness_Score',
        'GDP per capita': 'Economy_GDP_per_Capita',
        'Social support': 'Social_Support',
        'Healthy life expectancy': 'Health_Life_Expectancy',
        'Freedom to make life choices': 'Freedom',
        'Generosity': 'Generosity',
        'Perceptions of corruption': 'Corruption'
    }

    df.rename(columns=new_column_names, inplace=True)


def dropna_df(df):
    """
    Drops rows with NaN values in a DataFrame.
    """
    return df.dropna()


def drop_columns(df, columns_to_drop):
    """
    Drops specified columns from a DataFrame.
    """
    for column in columns_to_drop:
        if column in df.columns:
            df.drop([column], axis=1, inplace=True)


columns_to_drop_2015 = ['Region', 'Standard_Error', 'Dystopia_Residual']
columns_to_drop_2016 = ['Region', 'Lower Confidence Interval', 'Upper Confidence Interval', 'Dystopia_Residual']
columns_to_drop_2017 = ['Whisker_High', 'Whisker_Low', 'Dystopia_Residual']
