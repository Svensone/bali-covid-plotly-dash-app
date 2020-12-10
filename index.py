import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pathlib
# connect to main app.py file

from app import app
# from app import server

# connect to pages
from apps import bali, germany

background_img = ('/assets/Bali-Agung-Mountain.jpg')

app.layout = html.Div([
    html.Div(
        className='background-img',
        style={
        'verticalAlign': 'middle',
        'textAlign': 'center',
        'background-image': background_img,
        
        'width': '100%',
        'top': '0px',
        'left': '0px',
        'z-index': '1000'},
        children =[
        dcc.Location(id='url', refresh=False),
        html.Div(
            [
                dcc.Link('Bali Covid', href='/apps/bali'),
                dcc.Link('Germany Data', href='/apps/germany'),
            ]),
        html.Div(id='page-content')
    ])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def dispaly_page(pathname):
    if pathname == '/apps/bali':
        return bali.layout
    if pathname == '/apps/germany':
        return germany.layout
    else:
        return 'click a link to see the data'


if __name__ == '__main__':
    app.run_server(debug=True)
