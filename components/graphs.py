import dash_bootstrap_components as dbc
from dash import dcc, html
from config.constants import options_all

time_series = dbc.Card(
    (
        dbc.CardBody(
            [
                dcc.Graph(
                    id="time-series",
                    style={"height": 817},  # 815
                    config={"displaylogo": False, "displayModeBar": True},
                ),
            ],
        ),
    ),
    color="#f3f3f1",
)

scatter_plot_dd = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Select variable (x-axis):"),
            dcc.Dropdown(
                id="scatter-plot-dd-1",
                options=options_all,
                value="ISWR",
                clearable=False,
                style={"width": "90%"},
            ),
            html.Br(),
            html.H6("Select variable (y-axis):"),
            dcc.Dropdown(
                id="scatter-plot-dd-2",
                options=options_all,
                value="OSWR",
                clearable=False,
                style={"width": "90%"},
            ),
            html.Br(),
            html.H6("Select regression trendline:"),
            dcc.Dropdown(
                id="scatter-plot-dd-3",
                options=["OLS trendline", "LOWESS trendline"],
                value="OLS trendline",
                clearable=False,
                style={"width": "90%"},
            ),
            html.Br(),
            html.H6("Select multiple variables:"),
            dcc.Dropdown(
                id="scatter-matrix-dd",
                options=options_all,
                value=["ISWR", "OSWR", "TA1", "TA2"],
                clearable=False,
                multi=True,
                style={"width": "90%"},
            ),
        ]
    ),
    color="#f3f3f1",
)

scatter_plot = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(
                    id="scatter-plot",
                    style={"height": 500},
                    config={"displaylogo": False, "displayModeBar": True},
                ),
            ],
        ),
    ],
    color="#f3f3f1",
)

scatter_matrix = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(
                    id="scatter-matrix",
                    # style={'height': 500},
                    config={"displaylogo": False, "displayModeBar": True},
                ),
            ],
        ),
    ],
    className="mt-1",
    color="#f3f3f1",
)

scatter_plots = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(scatter_plot, width=10),
                dbc.Col(scatter_plot_dd, width=2),
            ],
            className="g-0",
        ),
        dbc.Row(
            [
                dbc.Col(scatter_matrix, width=12),
            ],
            className="g-0 border-0",
        ),
    ]
)

ridge_plot = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dcc.Graph(
                        id="ridge-plot",
                        style={"height": 500},
                        config={"displaylogo": False, "displayModeBar": True},
                    ),
                ],
            ),
        ],
        color="#f3f3f1",
    ),
)

violin_plot = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dcc.Graph(
                        id="violin-plot",
                        style={"height": 500},
                        config={"displaylogo": False, "displayModeBar": True},
                    ),
                ],
            ),
        ],
        className="mt-1",
        color="#f3f3f1",
    ),
)

violin_plots = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(ridge_plot),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(violin_plot),
            ],
        ),
    ]
)

uncertainty_test = dbc.Card(
    (
        dbc.CardBody(
            [
                dcc.Graph(
                    id="null-values",
                    style={"height": 500},
                    config={"displaylogo": False, "displayModeBar": True},
                ),
            ],
        ),
    ),
    color="#f3f3f1",
)
