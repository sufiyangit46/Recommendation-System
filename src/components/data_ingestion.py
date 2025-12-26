import pandas as pd
from src.logger import logging

class DataIngestion:
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Started")
        df=pd.read_csv('S:RestaurantData.csv')
        return df
