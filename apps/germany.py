
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

from app import app

import pathlib

##      1.3 App Layout
# ------------------------------------------------------------------------------

layout = html.Div([html.H3('App Germany'),])
