# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from tensorflow import keras
import dash_bootstrap_components as dbc


app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Fake News Classifier'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    html.Div(
        [
            html.I("Try typing in input 1 & 2, and observe how debounce is impacting the callbacks. Press Enter and/or Tab key in Input 2 to cancel the delay"),
            html.Br(),
            dcc.Input(id="article", type="text", placeholder="", style={'marginRight':'10px'}),
            dcc.Input(id="url", type="text", placeholder="", debounce=True),
            html.Div(id="output"),
        ]

    )

])

@app.callback(
    Output("output", "children"),
    Input("article", "value"),
    Input("url", "value"),
)
# def update_output(input1, input2):
#
#     return u'Input 1 {} and Input 2 {}'.format(input1, input2)

def update_output(input1, input2):
    print('running for {}'.format(input1))
    model = keras.models.load_model('C:/users/helen/OneDrive/Documents/GitHub/brianhelenfakenews/brianhelenfakenews/testing_stuff/saved_model')
    prediction = model.predict(input1)
    return 'input1 {}'.format(input1)

if __name__ == '__main__':
    app.run_server(debug=True)