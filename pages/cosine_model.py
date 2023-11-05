from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import pandas as pd

def calculate_cosine_similarity(df):
    # Drop non-numeric or non-relevant columns
    df_numeric = df.select_dtypes(include=[float, int])

    # Scale the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_numeric)

    # Calculate cosine similarity
    similarity = cosine_similarity(scaled_data)
    return similarity
