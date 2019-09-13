from flask import Flask, render_template, redirect, url_for
import pandas as pd
import requests
from pandas.io.json import json_normalize


app = Flask(__name__)

@app.route('/')
def front_page():
   return render_template('front_page.html')

@app.route('/titanic/<type>')
def titanic(type):
    if type == 'reversed':
        reversed_data = pd.read_csv('reversed.csv')
        reversed_data.drop('Unnamed: 0', inplace=True, axis=1)

        return render_template('titanic_view.html',tables=[reversed_data.to_html(classes='reversed')],
               titles = ['Reversed'])

    elif type == 'every_other':
        every_other_data = pd.read_csv('every_other.csv')
        every_other_data.drop('Unnamed: 0', inplace=True, axis=1)

        return render_template('titanic_view.html',tables=[every_other_data.to_html(classes='everyother')],
               titles = ['Every Other'])

    # return render_template('titanic_view.html',tables=[reversed_data.to_html(classes='reversed'), 
    #        every_other_data.to_html(classes='every_other')], titles = ['Reversed', 'Every Other'])
        

@app.route('/alphavantage')
def alphavantage():
    # Function for the alphavantage endpoint. Displays daily Microsoft info.

    # Calling this function to make sure we have an up-to-date dataset.
    alphavantage_msft()

    data = pd.read_excel('excel_output_normalized.xlsx')
    data.drop('Unnamed: 0', inplace=True, axis=1)
    data.set_index('Date', inplace=True)
    data = data.rename_axis(None)
    return render_template('alphavantage_view.html',tables=[data.to_html(classes='female')],
           titles = ['AlphaVantage Microsoft'])


def alphavantage_msft():
    # Script to pull from Microsoft daily series from the AlphaVantage API
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo'
    r = requests.get(url)
    data = r.content

    df = pd.read_json(data)
    df = df.iloc[6:]
    df = df.drop(['Meta Data'], axis=1)
    df = df.reset_index()
    df.columns = ['Date', 'Time Series (Daily)']

    df2 = df['Date']
    normalized = json_normalize(df['Time Series (Daily)'])
    df2 = pd.concat([df2, normalized], axis=1, sort=False)
    df2.columns = df2.columns.str.extract(r'([a-zA-Z]+)', expand=False)
    df2.columns = [x.capitalize() for x in df2.columns]

    # df.to_excel('excel_output.xlsx')
    df2.to_excel('excel_output_normalized.xlsx')
    
def titanic_data():
    # Function to transform training data for later use.
    df_titanic = pd.read_csv('train.csv')
    df_titanic_cols = df_titanic.columns.tolist()
    cols_rev = df_titanic_cols[::-1]
    df_titanic[cols_rev].to_csv('reversed.csv')
    every_other_cols = df_titanic.columns[::2]
    df_titanic[every_other_cols].to_csv('every_other.csv')


if __name__ == '__main__':
    #titanic_data()
    #alphavantage_msft()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0')