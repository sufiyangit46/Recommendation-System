import os
from src.components.data_preprocessing import preprocess_data
from src.components.recommender import build_similarity_model
from src.logger import logging

def run_training():
    logging.info('Training pipeline started')
    df=preprocess_data()

    logging.info('Data preprocessing completed')

    build_similarity_model(df)
    logging.info('Similarity model built successfully and saved')

if __name__ == '__main__':
    run_training()


