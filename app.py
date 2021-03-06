import dash
import dash_bootstrap_components as dbc

# meta_tags are required for the app layout to be mobile responsive

# add personal stylesheet '/assets/stylesheet.css'
external_stylesheets = [dbc.themes.DARKLY]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags= [{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}], suppress_callback_exceptions=True)

# test without meta_tags
# meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}]
            
server = app.server
