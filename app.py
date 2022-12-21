import dash_bootstrap_components as dbc
from dash import Dash
from components import navbar
from dash import callback, html, dcc
from dash.dependencies import Input, Output
from pages import about, main

# Initialize app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.YETI],
    title='GEUS | GCNVis',
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
    meta_tags=[
        {'name': 'viewport',
         'content': 'width=device-width, height=device-height, initial-scale=1.0, maximum-scale=1.2'
         }
    ]
)

# Navigation bar
navbar = navbar.create_navbar()

# Multi-page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', children=[]),
])


# Multi-page callback
@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return main.layout
    if pathname == '/about':
        return about.layout
    else:
        return main.layout


# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)  # Specify port with "port="
