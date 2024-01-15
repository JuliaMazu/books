import dash
from dash import html, Output, Input, State, callback, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1("Books", style={'textAlign': 'center', 'text-decoration' : 'underline overline #2c5f4d'}),
    dbc.Row([dbc.Col([dbc.Row(dcc.Input(id='author', type='text', placeholder='Authors name'),
                              style={'margin-top': '40px', 'margin-bottom' : '40px'}),
                      dbc.Row(dcc.Input(id='pages', type="number",
                                        min=0, max=7000, step=1,
                                        placeholder='Maximal number of pages')),
                      dbc.Row(dcc.Slider(id='rating', min=0, max=5, step=0.5, value=4.5), style={'margin-top' : '40px'}),
                      dbc.Row(html.Div([dbc.Button("I want to limit by rating", id="fade-button", className="mb-3", n_clicks=0, style={'margin-top' : '35px'}),                                                                                                                                                                
                                        dbc.Fade(
                                            dbc.Card(
                                                dbc.CardBody(
                                                    dcc.Input(id='votes', type="number",
                                                                min=0, max=4597666, step=100,
                                                                placeholder='Minimum number of votes'))),                                                                                                                                                                                                                                                                             
                                                id="fade",
                                                is_in=False,
                                                appear=False,),                                        
                                        ]
                                    ))                                                                                  
                                        ], style={'margin-left' : '50px'}),
            dbc.Col(dcc.Graph(id='books'), style={'flex' : '2'})])
])


@callback([Output('books', 'figure'),
           Output("fade", "is_in")],
              [Input('author', 'value'),
               Input('pages', 'value'),
               Input('votes', 'value'),
               Input('rating', 'value'),
               Input("fade-button", "n_clicks")
               ],
                [State("fade", "is_in")])
def update_graph(value_autor, value_pages, votes, rating, n, is_in):
    df = pd.read_csv('books.csv', on_bad_lines='skip')
    df = df[df['average_rating']>=rating].reset_index()
    if value_autor is not None:
        df = df[df['authors'].str.contains(value_autor, case=False)].reset_index()
    if value_pages is not None:
        df = df[df['  num_pages']>=value_pages].reset_index()
    if votes is not None:
        df = df[df['ratings_count']>=votes].reset_index()

    books = px.bar(df.loc[:10], x = 'title', y = '  num_pages', labels={
                     "  num_pages": "Number of pages",
                     "title": "Title"
                     })


    books.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    books.update_yaxes(title_font_color="black", color="black", title_font_size=14)
    books.update_xaxes(title_font_color="black", color="black", title_font_size=14,
                   tickangle=45, tickvals = df['title'][:10],
                   ticktext= [i[:15] for i in df.loc[:10, 'title'] ])
    if not n:
        # Button has never been clicked
        return books, False
    return books, not is_in