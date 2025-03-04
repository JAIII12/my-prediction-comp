from sklearn.base import TransformerMixin, BaseEstimator
import numpy as np
import pandas as pd


class Clean_and_Merge(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, df, y=None):
        return self
    
    def transform(self, df, y=None):
        categorical_attributes = ['preferred_foot', 'attacking_work_rate', 'defensive_work_rate']

        numercial_attributes = ['potential', 'crossing', 'finishing', 'heading_accuracy',
            'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
            'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
            'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
            'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
            'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
            'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
            'gk_reflexes']
        player_id = df['player_fifa_api_id'].unique()

new_df_list = []

for i in player_id:
    filtered_df = df[df['player_fifa_api_id'] == i]

    temp_num = filtered_df[numercial_attributes].mean()
    temp_cat = filtered_df[categorical_attributes].mode().squeeze()
    temp_cat = temp_cat.fillna("Unknown")  # Handle missing modes

    temp_df = pd.DataFrame({**temp_num.to_dict(), **temp_cat.to_dict()}, index=[0])

    new_df_list.append(temp_df)

new_df = pd.concat(new_df_list, ignore_index=True)
