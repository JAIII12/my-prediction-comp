import sqlite3
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error 
from math import sqrt
from datetime import datetime

cnx = sqlite3.connect('data/database.sqlite')
player_data = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)
print(player_data.head())

