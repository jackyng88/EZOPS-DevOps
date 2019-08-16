import requests
import pandas as pd
from pandas.io.json import json_normalize


# Script to pull from the AlphaVantage API

# Pull from API to get a time series of daily quotes for Mirosoft.
# apikey = EUGCFTPCWVEJRFPD
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo'
r = requests.get(url)
data = r.content

# df is a DataFrame with the raw JSON data converted to it
df = pd.read_json(data)
# Drop the first 6 rows which are all metadata
df = df.iloc[6:]
# Drop the empty (NaN) metadata column
df = df.drop(['Meta Data'], axis=1)
df = df.reset_index()
df.columns = ['Date', 'Time Series (Daily)']


# Creating a new DataFrame df2 that has the Date column from df and then merge
# it with the normalized JSON/Dictionary columns so it has open, high, low, 
# close, and volume as columns instead of remaining as key values in a dict.
df2 = df['Date']
normalized = json_normalize(df['Time Series (Daily)'])
df2 = pd.concat([df2, normalized], axis=1, sort=False)
# Removing the numbers from the column names and then capitalizing the first
# letter i.e. '1. open' -> 'Open'
df2.columns = df2.columns.str.extract(r'([a-zA-Z]+)', expand=False)
df2.columns = [x.capitalize() for x in df2.columns]

df.to_excel('excel_output.xlsx')
df2.to_excel('excel_output_normalized.xlsx')
print(df2)