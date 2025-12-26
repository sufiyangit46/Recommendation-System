import os
import pandas as pd
from src.logger import logging
from sklearn.preprocessing import OneHotEncoder
from src.utils import save_object, compute_cosine_similarity

def build_similarity_model(df):
    try:
        features=['Cuisines','Price range','Has Online delivery']

        encoder=OneHotEncoder(handle_unknown='ignore',sparse_output=False)
        feature_matrix=encoder.fit_transform(df[features])

        similarity_matrix=compute_cosine_similarity(feature_matrix)

        os.makedirs('artifacts',exist_ok=True)

        save_object('artifacts/encoder.pkl',encoder)
        save_object('artifacts/similarity_matrix.pkl',similarity_matrix)
        save_object('artifacts/feature_matrix.pkl',feature_matrix)
        save_object('artifacts/data.pkl',df)
        logging.info("Artifacts Saved successfully")

    except Exception as e:
        logging.error(f'Error in building similarity model: {e}')
        raise

