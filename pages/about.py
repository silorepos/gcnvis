import dash_bootstrap_components as dbc
from dash import html

layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4("About this website", className="card-title"),
                                html.P(
                                    "This website aims to support the ongoing analysis and processing of the L1 data from the "
                                    "GC-Net (see below). By providing an interactive and user-friendly visualization "
                                    "environment, it enables researchers to explore processed data in new and interesting "
                                    "ways. The website has two main sections: a data settings panel on the left side, "
                                    "and a group of tabs for visualizing the data on the right side. The data settings panel "
                                    "allows users to select a specific station, a year range, and to filter the data by key "
                                    "variables. All of the interactive plots on the right side update automatically when the "
                                    "data settings are changed.",
                                    className="card-text",
                                ),
                                html.Br(),
                                html.H4("About the GC-Net", className="card-title"),
                                html.P(
                                    "The Greenland Climate Network (GC-Net) is a set of Automatic Weather Stations (AWS) that "
                                    "were set up and managed by the late Konrad (Koni) Steffen. The network began with a "
                                    "single station in 1991, and is now the longest running climatological record of "
                                    "Greenland. Spanning the ice sheet, each AWS measures temperature, radiation, "
                                    "wind speed/direction, humidity and several other variables. Since 2021, the GC-Net has "
                                    "been maintained by the Geological Survey of Denmark and Greenland (GEUS).",
                                    className="card-text",
                                ),
                                html.Br(),
                                html.H4("About the data", className="card-title"),
                                html.P(
                                    "This dataset consists of two main data levels: level 0 (L0) and level 1 (L1). L0 is the "
                                    "raw data from the dataloggers, historical processing codes, satellite transmissions, "
                                    "and Koni's personal data archive. L1 is the appended, calibrated, cleaned, and quality "
                                    "flagged data. It is provided in the newly described Non-Binary Environmental Data "
                                    "Archive (NEAD) format, which is also CSV-compatible.",
                                    className="card-text",
                                ),
                            ]
                        ),
                    ],
                    color="dark",
                    inverse=True,
                    outline=False,
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    html.H4(
                                        children="Access the data processing scheme here:",
                                        className="text-left",
                                    ),
                                    dbc.Button(
                                        "Open GitHub",
                                        href="https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing",
                                        color="dark",
                                    ),
                                ],
                                body=True,
                                color="dark",
                                outline=True,
                            ),
                            width=6,
                        ),
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    html.H4(
                                        children="Download the latest L1 data here:",
                                        className="text-left",
                                    ),
                                    dbc.Button(
                                        "Open GitHub",
                                        href="https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing/tree/main/L1",
                                        color="dark",
                                    ),
                                ],
                                body=True,
                                color="dark",
                                outline=True,
                            ),
                            width=6,
                        ),
                    ],
                ),
            ]
        )
    ]
)
