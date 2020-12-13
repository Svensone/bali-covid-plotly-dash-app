
# Bali Covid-Cases per Regency Dash Web App

import pandas as pd
# import numpy as np
import json

import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app

import pathlib

# ------------------------------------------------------------------------------
# 1. Data
# ------------------------------------------------------------------------------
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath('../datasets').resolve()

# ------------------------------------------------------------------------------
# 1. App Layout
# ------------------------------------------------------------------------------
# 1.1 CSS Styles
# ------------------------------------------------------------------------------

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 20,
    'left': 0,
    'bottom': 0,
    'width': '25%',
    'padding': '10px 10p',
    'background-color': '#f8f9fa'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '5%',
    'margin-right': '5%',
    'padding': '10px 10p',

}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': 'primary'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': 'primary'
}

# 1.2 Html Components
# ------------------------------------------------------------------------------


controls = dbc.FormGroup(
    [
        html.H2('Map', style=TEXT_STYLE),
        html.Hr(),
        html.P('Pick a Date', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(
            id='dropdown_date',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            }, {
                'label': 'Value Two',
                'value': 'value2'
            },
                {
                    'label': 'Value Three',
                    'value': 'value3'
            }
            ],
            value=['value1'],  # default value
            multi=True
        ),
        html.Br(),

        html.P('Cases', style={
            'textAlign': 'center'
        }),
        dbc.Card([dbc.Checklist(
            id='check_list_cases',
            options=[{
                'label': 'Deaths',
                'value': 'value1'
            },
                {
                    'label': 'Recovered',
                    'value': 'value2'
            },
                {
                    'label': 'Active Cases',
                    'value': 'value3'
            }
            ],
            value=['value1', 'value2'],
            inline=True
        )]),
        html.Br(),
        html.H2('Bar Graph', style=TEXT_STYLE),
        html.Hr(),
        html.P('Pick a County', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(
            id='dropdown_county',
            options=[{
                'label': 'Bali ',
                'value': 'value1'
            }, {
                'label': 'Denpasar',
                'value': 'value2'
            },
                {
                    'label': 'Badung',
                    'value': 'value3'
            },
                {
                    'label': 'Gianyiar',
                    'value': 'value4'
            },
                {
                    'label': 'Bangli',
                    'value': 'value5'
            },
                {
                    'label': 'Jembrana',
                    'value': 'value6'
            },
                {
                    'label': 'Buleleng',
                    'value': 'value7'
            },
                {
                    'label': 'Karangasem',
                    'value': 'value8'
            },
                {
                    'label': 'Foreigners',
                    'value': 'value3'
            }
            ],
            value=['value1'],  # default value
            multi=True
        ),
        html.Br(),
        dbc.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit',
            color='primary',
            block=True
        ),
    ]
)

# sidebar Component
sidebar = html.Div(
    [
        html.Br(),
        html.Hr(),
        html.H2('Parameters', style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)

# content row Components
content_first_row = dbc.Row([
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4(id='card_title_1', children=['Total Cases per Regency'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P(id='card_text_1', children=[
                               'Total Positive Cases/ daily new cases'], style=CARD_TEXT_STYLE),
                        html.Br(),
                        dbc.Button(
                            id='submit_button',
                            n_clicks=0,
                            children='Show Cases',
                            color='primary',
                            block=True
                        ),
                    ]
                )
            ]
        ),
        md=6
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Bali Cases', className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P('Cases per Regency', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=6
    )

])

content_second_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_1'), md=12,
        ),

    ]
)

content_third_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_4'), md=12,
        )
    ]
)

# Content Component
content = html.Div([
    html.Br(),
    html.Hr(),
    html.H2('Bali Daily Covid Cases', style=TEXT_STYLE),
    html.Hr(),
    content_first_row,
    content_second_row,
    content_third_row,
],
    style=CONTENT_STYLE
)


# 1.3 App Layout
# ------------------------------------------------------------------------------

layout = html.Div([
    # sidebar,
    content
])

# ------------------------------------------------------------------------------
# 2. Connect Layout with Callback
# ------------------------------------------------------------------------------


@ app.callback(
    Output('graph_1', 'figure'),
    Input('submit_button', 'n_clicks'),
)
def update_graph_1(n_clicks): 
    # print(n_clicks)

    # Bar Chart new and total cases per regency
    # path_data = r'C:\Users\ansve\Coding\Projects-DataScience\2020.12.05-Bali_Covid_Dash_App\Data'

    df_bali = pd.read_excel(DATA_PATH.joinpath('regencyCasesBali.xlsx'))

    fig = px.bar(df_bali, x='Regency', y='total cases', hover_data=[
        'Regency', 'new cases total', 'total cases'], text='new cases total')

    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',
                      )
    fig.update_layout({
        'height': 400
    })
    return fig


@ app.callback(
    Output('graph_4', 'figure'),
    [Input('submit_button', 'n_clicks')],
    )
def update_graph_4(n_clicks):
    print(n_clicks)

    # Bali Regency Covid Cases

    df_bali = pd.read_excel(DATA_PATH.joinpath('regencyCasesBali.xlsx'))
    geojson_bali = json.load(
        open(DATA_PATH.joinpath('bali_geojson_id.geojson'), 'r'))

    fig = px.choropleth_mapbox(df_bali, geojson=geojson_bali, locations='id', color='log10 total cases',
                               mapbox_style='carto-positron', hover_name='Regency', hover_data=['new cases total', 'total cases'],
                               title='Covid Cases in Bali per Regency', zoom=8, center={"lat": -8.5002, "lon": 115.0129},
                               opacity=0.5,)

    fig.update_layout({
        'height': 800
    })
    return fig


@ app.callback(
    Output('card_title_1', 'children'),
    [Input('submit_button', 'n_clicks')],
    )
def update_card_title_1(n_clicks):
    print(n_clicks)
    
    # Sample data and figure
    return 'Bali Cases total and daily new'


@ app.callback(
    Output('card_text_1', 'children'),
    [Input('submit_button', 'n_clicks')],
    )
def update_card_text_1(n_clicks):
    print(n_clicks)
    
    # Sample data and figure
    return 'showing data from input'
