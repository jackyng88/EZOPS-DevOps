import numpy as np
import pandas as pd


# Loading the csv into a pandas DataFrame
df_titanic = pd.read_csv('train.csv')

# The DataFrame columns in list form
df_titanic_cols = df_titanic.columns.tolist()

# Output csv file with the reverse order for the columns
cols_rev = df_titanic_cols[::-1]
df_titanic[cols_rev].to_csv('reversed.csv')

# Output csv file with every other column
every_other_cols = df_titanic.columns[::2]
df_titanic[every_other_cols].to_csv('every_other.csv')
