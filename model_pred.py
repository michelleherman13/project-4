import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

class ModelPred():
    def __init__(self):
        pass

    def get_recommended(df, game, n_neighbors=10):
        df = pd.read_csv("resources/vgames_rec.csv").drop('Unnamed: 0', axis=1)
        info_df = pd.read_csv("resources/vgames_clean.csv").drop('Unnamed: 0', axis=1)

        df.drop_duplicates(subset ="game").reset_index().drop('index', axis=1)
        info_df = info_df.drop_duplicates(subset ="game").reset_index().drop('index', axis=1)

        df_sub = df.drop(["game"], axis=1)
        model_knn = NearestNeighbors(metric='jaccard', n_neighbors=n_neighbors)
        model_knn.fit(df_sub)
        
        game_row = df.loc[df["game"] == game].head(1)
        gr = df.loc[df["game"] == game].head(1) # for index value of game
        game_row = game_row.drop(["game"], axis=1)
        game_row = game_row.to_numpy()
        
        distances, indices = model_knn.kneighbors(game_row, n_neighbors = n_neighbors)
        gri = np.where(indices == gr.index)[1] # variable to hold game's index value in indices
        indices = indices[indices != gr.index] # drops input game if it is in indices array
        result = info_df.iloc[indices.flatten()].to_json(orient='records')
        
        return result

    def get_recommended2(df, platform, score=0, n_neighbors=10):
        df = pd.read_csv("resources/vgames_rec.csv").drop('Unnamed: 0', axis=1)
        info_df = pd.read_csv("resources/vgames_clean.csv").drop('Unnamed: 0', axis=1)

        df.drop_duplicates(subset ="game").reset_index().drop('index', axis=1)
        info_df = info_df.drop_duplicates(subset ="game").reset_index().drop('index', axis=1)

        platform = f'Platform_{platform}'

        df_sub = df.drop(["game"], axis=1)
        model_knn = NearestNeighbors(metric='cosine', n_neighbors=n_neighbors)
        model_knn.fit(df_sub)
        
        game_row = df[(df[platform] == 1) & (df['Critic_Score'] >= score)].sample(1)
        game_row = game_row.drop(["game"], axis=1)
        game_row = game_row.to_numpy()
        platform = platform.replace("Platform_", "")


        distances, indices = model_knn.kneighbors(game_row, n_neighbors = n_neighbors)
        result = info_df.iloc[indices.flatten()]#.to_json(orient='records')
        result = result[(result['Platform'] == platform) & (result['Critic_Score'] > score)].to_json(orient='records')

        return result