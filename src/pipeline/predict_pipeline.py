import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class PredictPipeline:
    def recommend(self,user_input,df,top_n=5):

        with open('artifacts/encoder.pkl', 'rb') as f:
            encoder = pickle.load(f)

        with open('artifacts/similarity_matrix.pkl', 'rb') as f:
            similarity_matrix = pickle.load(f)

        user_df=pd.DataFrame([user_input])
        user_vector=encoder.transform(user_df)

        similarity=cosine_similarity(user_vector,encoder.transform(df[['Cuisines','Price range','Has Online delivery']]))
        top_indices=similarity[0].argsort()[:top_n]

        return df.iloc[top_indices][['Restaurant Name','Cuisines','Aggregate rating']]
