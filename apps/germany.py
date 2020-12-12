
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

# 1 Data
# ------------------------------------------------------------------------------

PATH = pathlib.Path(__file__).parent
path_csv = PATH.joinpath('../datasets/county_covid_BW.csv')
path_geojson = PATH.joinpath('../datasets/geojson_ger.json')

df = pd.read_csv(path_csv)
geojson = json.load(open(path_geojson, 'r'))


# 2 Layout
# ------------------------------------------------------------------------------

# 2.1 CSS Styles
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
    'margin-left': '25%',
    'margin-right': '5%',
    'padding': '10px 10p'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}


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
                        html.H4(id='card_title_2', children=['Total Cases per County'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P(id='card_text_2', children=[
                               'Total Positive Cases/ daily new cases'], style=CARD_TEXT_STYLE),
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
                        html.H4('Baden-Wuerttemberg (Germany) Cases', className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P('Cases per County', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=6
    ),

])

content_second_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_2'), md=12
        ),

    ]
)

content_third_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_3'), md=12,
        )
    ]
)
# Background Image Div

# html.Div(
#     style={
#         'verticalAlign': 'middle',
#         'textAlign': 'center',
#         'background-image': background_img,
#         'position': 'fixed',
#         'width': '100%',
#         'height': '100%',
#         'top': '0px',
#         'left': '0px',
#         'z-index': '1000'},
# Content Component

content = html.Div([
        html.Br(),
        html.Hr(),
        html.H2('Baden-Wuerttemberg Daily Covid Cases', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row,
    ],
    style=CONTENT_STYLE
)


layout = html.Div([
    sidebar,
    content
])


# 3 Callbacks
# ------------------------------------------------------------------------------

@ app.callback(
    Output('graph_2', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('check_list_cases', 'value'),
     State('dropdown_county', 'value')
     ])
def update_graph_2(n_clicks, dropdown_county_value, check_list_value):
    print(n_clicks)
    print(dropdown_county_value)
    print(check_list_value)

    fig = px.bar(df, x="GEN", y='cases', hover_data=[
                 'cases7_per_100k', 'death_rate'])

    fig.update_layout({
        'height': 400
    })
    return fig


@ app.callback(
    Output('graph_3', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('check_list_cases', 'value'),
     State('dropdown_county', 'value')
     ])
def update_graph_3(n_clicks, dropdown_county_value, check_list_value):
    print(n_clicks)
    print(dropdown_county_value)
    print(check_list_value)

    fig = px.choropleth_mapbox(df,
                               geojson=geojson, locations='id',
                               color='cases7_per_100k', color_continuous_scale='blues',
                               hover_name='GEN',
                               hover_data=['cases_per_100k',
                                           'cases7_bl_per_100k'],
                               title='Cases per County in State Baden Wuerttemberg',
                               opacity=0.8,
                               zoom=5,
                               mapbox_style='carto-positron',
                               center={'lat': 48.11003112792969,
                                       'lon': 8.65347957611084}
                               )
    fig.update_layout({
        'height': 800
    })
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    # fig.update_geos(fitbounds = 'locations', visible = False)
    return fig

@ app.callback(
    Output('card_title_2', 'children'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown_date', 'value'), State('check_list_cases', 'value'),
     State('dropdown_county', 'value'),
     ])
def update_card_title_2(n_clicks, dropdown_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(check_list_value)
    # Sample data and figure
    return ' Germany County Cases and daily new'


@ app.callback(
    Output('card_text_2', 'children'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown_date', 'value'), State('check_list_cases', 'value'),
     State('dropdown_county', 'value'),
     ])
def update_card_text_2(n_clicks, dropdown_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(check_list_value)
    # Sample data and figure
    return 'showing data from input'