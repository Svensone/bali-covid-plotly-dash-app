import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
import pathlib

# connect to main app.py file
from app import app
from app import server

# connect to pages
from apps import bali, germany

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink('the blonde Bali Boy', href="https://svenson-bali-homepage.netlify.app/index.html")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem('Bali', href='/apps/bali',),
                dbc.DropdownMenuItem('Germany', href='/apps/germany'),
                dbc.DropdownMenuItem('to be continued ...', href='#')
            ],
            nav=True,
            in_navbar=True,
            label="More",
            color='light',
        )
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    # dark=True,
)
app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        navbar,
        # html.Div(
        #     [
        #         dcc.Link('Bali Covid', href='/apps/bali'),
        #         dcc.Link('Germany Data', href='/apps/germany'),
        #     ]),
        html.Div(id='page-content')
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
