# Placeholder for recommender utilities (if you want to expand)
def get_top_jobs(similarity_scores, df, top_n=5):
    idx = similarity_scores.argsort()[-top_n:][::-1]
    return df.iloc[idx]
