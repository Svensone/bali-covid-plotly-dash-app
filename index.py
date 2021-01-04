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


# CSS Styles
# ------------------------------------------------------------------------------
CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': 'primary'
}
CONTENT_STYLE = {
    'margin-left': '5%',
    'margin-right': '5%',
    'margin-top': '5%',
    'padding': '10px 10p',

}
# HTML Components
# ------------------------------------------------------------------------------

# Navigation Bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink('About me - Blonde-Bali-Boy',
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

# Cards (Links) and General Info
content_row_1 = dbc.Row([
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4(id='card_bali', children=['Bali Cases'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.A('see more', style=CARD_TEXT_STYLE,
                               href='/apps/bali')
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
                        html.H4('Germany Cases', className='card-title',
                                style=CARD_TEXT_STYLE),
                        # , target="_blank"
                        html.A("see more", href='/apps/germany'),
                    ]
                ),
            ]
        ),
        md=6
    )

], style=CONTENT_STYLE
)

content_row_2 = dbc.Row([
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4(id='card_info', children=['Workflow'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P('see more', style=CARD_TEXT_STYLE,
                               )
                    ]
                )
            ]
        ),
        md=12
    )

], style=CONTENT_STYLE
)

app.layout = html.Div(
    style={
        'background-image': 'url("/assets/bg3.jpg")',
        'background-position': 'center',
        'background-size': 'cover',
    },
    children=[
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
                'height': '1000px',
                'top': '10%',
            },
            children=[
                content_row_1,
                content_row_2
            ]
        )


if __name__ == '__main__':
    app.run_server(debug=True)
