import dash
from dash import Dash, html, dcc
from dash import Dash, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
from dash_iconify import DashIconify

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SKETCHY])


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "12rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H6("Navigation", style={'font-size' : '30px'}),
        html.Hr(),
        html.P(
            "To find out about the most fascinating thing - books", className="lead"
        ),
        dbc.Nav(
            [   dmc.NavLink("Basic info", href="/",
                  label="Home",
                  icon=DashIconify(icon="bi:house-door-fill", height=16, color="#c2c7d0")
                            ),
                dmc.NavLink("To find a book of your heart", href="/fav",
                  label="Favorites",
                  icon=DashIconify(icon="pepicons-print:heart-filled", height=16, color="#c2c7d0")
                            ),
                dmc.NavLink("Book analytics", href="/analysis",
                  label="Books",
                  icon=DashIconify(icon="raphael:book", height=16, color="#c2c7d0")
                            )
                
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


app.layout = dbc.Container([dbc.Col(sidebar), 
                            dbc.Col(dash.page_container, style=CONTENT_STYLE) ])




if __name__ == '__main__':
    app.run(debug=True)