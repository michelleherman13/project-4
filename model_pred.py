import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import NearestNeighbors

class ModelPred():
    def __init__(self):
        pass

    def get_recommended(df, game, n_neighbors=10):
        df_sub = df.drop(["game"], axis=1)
        df = pd.read_csv("resources/vgames_rec.csv")

        if game != '':
            #add filters here 
            model_knn = NearestNeighbors(metric='jaccard', n_neighbors=n_neighbors)
            model_knn.fit(df_sub)
            
            game_row = df.loc[df["game"] == game].head(1)
            gr = df.loc[df["game"] == game].head(1) # for index value of game
            game_row = game_row.drop(["game"], axis=1)
            game_row = game_row.to_numpy()
            
            distances, indices = model_knn.kneighbors(game_row, n_neighbors = n_neighbors)
            gri = np.where(indices == gr.index)[1] # variable to hold game's index value in indices
            indices = indices[indices != gr.index] # drops input game if it is in indices array
            result = df.iloc[indices.flatten()]
            distances = np.delete(distances, gri) # drops input game from distances array
            result["Distance"] = distances
            
            return result