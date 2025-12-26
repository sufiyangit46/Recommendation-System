import pandas as pd
from src.logger import logging

def preprocess_data():
    try:
        df=pd.read_csv('S:RestaurantData.csv')
        logging.info("Dataset loaded")

        df=df[[
            'Restaurant Name',
            'Cuisines',
            'Price range',
            'Has Online delivery'
        ]]

        df.dropna(inplace=True)

        return df

    except Exception as e:
        logging.error(f'Preprocessing Error: {e}')
        raise
