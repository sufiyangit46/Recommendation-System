import os
import dill
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def save_object(file_path,obj):
    os.makedirs(os.path.dirname(file_path),exist_ok=True)
    with open(file_path,'wb') as file_obj:
        dill.dump(obj,file_obj)

def load_object(file_path):
    with open(file_path,'rb') as file_obj:
        return dill.load(file_obj)

def compute_cosine_similarity(matrix):
    return cosine_similarity(matrix)
