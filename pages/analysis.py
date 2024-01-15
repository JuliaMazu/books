import dash
from dash import Dash, html, dcc
from dash import Dash, Input, Output, callback, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dash.register_page(__name__,
    title='Our Analytics Dashboard',
    name='Our Analytics Dashboard')

layout = dbc.Container([
    html.Div(html.H1('The most appreciated books, authors, publishers'), style={'textAlign': 'center', 'text-decoration' : 'underline overline #2c5f4d'}),
    html.Div([dbc.Row([dbc.Col([dbc.Button( "Authors", id='autors',color="danger", className="me-1", n_clicks=0 )]),
                     dbc.Col([dbc.Button('Publishers', id='publisher', color='info', className="me-2", n_clicks=0)]),
                     dbc.Col([dbc.Button('Books', id='book', color='success', className="me-3", n_clicks=0)])
    ])], style={"margin-top" : '50px', 'textAlign' : 'center'}),
    dbc.Row(html.Span(id='example-output'))    
])


@callback(
    Output("example-output", "children"), 
    [Input("autors", "n_clicks"),
    Input('publisher', 'n_clicks'),
    Input('book', 'n_clicks')]
)
def on_button_click(a, p, b):
        return a+p+b