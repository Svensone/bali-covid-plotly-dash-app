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
        dbc.NavItem(dbc.NavLink('About Me - the blonde Bali Boy',
                                href="https://svenson-bali-homepage.netlify.app/index.html")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem('Bali', href='/apps/bali',),
                dbc.DropdownMenuItem('Germany', href='/apps/germany'),
                dbc.DropdownMenuItem('to be continued ...',
                                     href='/apps/testDashboard')
            ],
            nav=True,
            in_navbar=True,
            label="More",
            color='light',
        )
    ],
    brand="Home",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = html.Div(
    style={
        'background-image': 'url("/assets/bg3.jpg")',
        'background_position': 'center',
        'background-repeat': 'no-repeat',
        'background-size': 'cover',

    }, children=[

        dcc.Location(id='url', refresh=False),
        navbar,
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
        return html.Div(
            style={
                'verticalAlign': 'middle',
                'textAlign': 'center',
                # 'background-image': 'url("/assets/bg1.jpg")',
                'background_position': 'center',
                # 'background-repeat': 'no-repeat',
                'background-size': 'auto',
                # 'position': 'fixed',
                'width': '100px',
                'height': '1000px',
                'top': '10%',
                'left': '0px',
                # 'z-index': '1000'
            }
        )


if __name__ == '__main__':
    app.run_server(debug=True)
