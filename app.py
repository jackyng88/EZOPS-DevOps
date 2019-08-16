from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

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


    data = pd.read_excel('excel_output_normalized.xlsx')
    data.drop('Unnamed: 0', inplace=True, axis=1)
    data.set_index('Date', inplace=True)
    data = data.rename_axis(None)
    return render_template('alphavantage_view.html',tables=[data.to_html(classes='female')],
           titles = ['AlphaVantage Microsoft'])

    


if __name__ == '__main__':
   app.run(debug=True)