
## Bali Covid-Cases per Regency Dash Web App

import pandas as pd
# import numpy as np
import json

import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

# ------------------------------------------------------------------------------
## 1. App Layout
# ------------------------------------------------------------------------------
##      1.1 CSS Styles
# ------------------------------------------------------------------------------

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'padding': '20px 10p'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

##      1.2 Html Components
# ------------------------------------------------------------------------------

controls = dbc.FormGroup(
    [
        html.P('Dropdown', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(
            id='dropdown',
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
        html.P('Range Slider', style={
            'textAlign': 'center'
        }),
        dcc.RangeSlider(
            id='range_slider',
            min=0,
            max=20,
            step=0.5,
            value=[5, 15]
        ),
        html.P('Check Box', style={
            'textAlign': 'center'
        }),
        dbc.Card([dbc.Checklist(
            id='check_list',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            },
                {
                    'label': 'Value Two',
                    'value': 'value2'
                },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value=['value1', 'value2'],
            inline=True
        )]),
        html.Br(),
        html.P('Radio Items', style={
            'textAlign': 'center'
        }),
        dbc.Card([dbc.RadioItems(
            id='radio_items',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            },
                {
                    'label': 'Value Two',
                    'value': 'value2'
                },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value='value1',
            style={
                'margin': 'auto'
            }
        )]),
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
                        html.H4(id='card_title_1', children=['Card Title 1'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P(id='card_text_1', children=['Sample text.'], style=CARD_TEXT_STYLE),
                    ]
                )
            ]
        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Card Title 2', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 3', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 4', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]
        ),
        md=3
    )
])

content_second_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_1'), md=4
        ),
        dbc.Col(
            dcc.Graph(id='graph_2'), md=4
        ),
        dbc.Col(
            dcc.Graph(id='graph_3'), md=4
        )
    ]
)

content_third_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_4'), md=12,
        )
    ]
)

content_fourth_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_5'), md=6
        ),
        dbc.Col(
            dcc.Graph(id='graph_6'), md=6
        )
    ]
)
# Content Component
content = html.Div(
    [
        html.H2('Bali Daily Covid Cases', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row,
        # content_fourth_row
    ],
    style=CONTENT_STYLE
)


##      1.3 Inititalise App and create App Layout
# ------------------------------------------------------------------------------

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server # for heroku deployment

app.layout = html.Div([sidebar, content])

# ------------------------------------------------------------------------------
## 2. Connect Layout with Callback
# ------------------------------------------------------------------------------
@app.callback(
    Output('graph_1', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_graph_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)

    # Bar Chart new and total cases per regency
    # path_data = r'C:\Users\ansve\Coding\Projects-DataScience\2020.12.05-Bali_Covid_Dash_App\Data'
    
    df_bali = pd.read_excel('Data/regencyCasesBali.xlsx')

    fig = px.bar(df_bali, x='Regency', y='total cases', hover_data=['Regency', 'new cases total', 'total cases'], text='new cases total')

    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    return fig


@app.callback(
    Output('graph_2', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_graph_2(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)
    fig = {
        'data': [{
            'x': [1, 2, 3],
            'y': [3, 4, 5],
            'type': 'bar'
        }]
    }
    return fig


@app.callback(
    Output('graph_3', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_graph_3(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)
    df = px.data.iris()
    fig = px.density_contour(df, x='sepal_width', y='sepal_length')
    return fig


@app.callback(
    Output('graph_4', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_graph_4(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)  
    ## Bali Regency Covid Cases 

    # Sample data and figure
    # path_data = r'C:\Users\ansve\Coding\Projects-DataScience\2020.12.05-Bali_Covid_Dash_App\Data'
    df_bali = pd.read_excel('Data/regencyCasesBali.xlsx')
    geojson_bali = json.loaD('Data/bali_geojson_id.geojson', 'r'))
    
    fig = px.choropleth_mapbox(df_bali, geojson= geojson_bali, locations='id', color='log10 total cases',
    mapbox_style= 'carto-positron', hover_name= 'Regency', hover_data=['new cases total', 'total cases'],
                    title='Covid Cases in Bali per Regency', zoom=8, center = {"lat": -8.2902, "lon": 114.8129},
                    opacity=0.5,)
    # df = px.data.gapminder().query('year==2007')
    # fig = px.scatter_geo(df, locations='iso_alpha', color='continent',
                        #  hover_name='country', size='pop', projection='natural earth')
    
    
    fig.update_layout({
        'height': 600
    })
    return fig


# @app.callback(
#     Output('graph_5', 'figure'),
#     [Input('submit_button', 'n_clicks')],
#     [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
#      State('radio_items', 'value')
#      ])
# def update_graph_5(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
#     print(n_clicks)
#     print(dropdown_value)
#     print(range_slider_value)
#     print(check_list_value)
#     print(radio_items_value)  # Sample data and figure
#     df = px.data.iris()
#     fig = px.scatter(df, x='sepal_width', y='sepal_length')
#     return fig


# @app.callback(
#     Output('graph_6', 'figure'),
#     [Input('submit_button', 'n_clicks')],
#     [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
#      State('radio_items', 'value')
#      ])
# def update_graph_6(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
#     print(n_clicks)
#     print(dropdown_value)
#     print(range_slider_value)
#     print(check_list_value)
#     print(radio_items_value)  # Sample data and figure
#     df = px.data.tips()
#     fig = px.bar(df, x='total_bill', y='day', orientation='h')
#     return fig


@app.callback(
    Output('card_title_1', 'children'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_card_title_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)  # Sample data and figure
    return 'Card Tile 1 change by call back'


@app.callback(
    Output('card_text_1', 'children'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
     State('radio_items', 'value')
     ])
def update_card_text_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    print(n_clicks)
    print(dropdown_value)
    print(range_slider_value)
    print(check_list_value)
    print(radio_items_value)  # Sample data and figure
    return 'Card text change by call back'



# ------------------------------------------------------------------------------
## 4. Run App
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    # app.run_server(port='8085') # if run locally
    app.run_server(debug=True) # for deployment on heroku
