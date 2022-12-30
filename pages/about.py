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
                                    "GCNVis aims to support the ongoing analysis of the GC-Net data. "
                                    ""
                                    "We present an interactive visualization tool with "
                                    "dynamic filter controls, linked views and historical data that ranges back to "
                                    "the very first measurements. The mainpage consists of three sections: a data "
                                    "settings panel, an interactive map and a group of tabs with relevant "
                                    "visualizations. The data settings panel "
                                    "allows users to select a specific station, a year range and filter the data "
                                    "by "
                                    "categories or customized variables of interest. The map and visualizations will then "
                                    "update accordingly, providing a synergistic effect between interactive "
                                    "exploration and comparative analysis. ",
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
                                    "The dataset has two main data levels: level 0 (L0) and level 1 (L1). L0 is the "
                                    "raw data from the dataloggers, historical processing codes, satellite transmissions, "
                                    "and Koni's personal data archive. L1 is the appended, calibrated, cleaned, and quality "
                                    "flagged data. It is provided in the newly described Non-Binary Environmental Data "
                                    "Archive (NEAD) format, which is also CSV-compatible. Links for the full processing scheme "
                                    "and the latest L1 data are provided below. ",
                                    className="card-text",
                                ),
                                # html.Img(
                                #     src="https://eng.geus.dk/Media/D/B/GC-Net%20AWS%202005%20after%20raising%20tower.JPG", height="500px", )
                                dbc.CardImg(
                                    src="https://eng.geus.dk/Media/D/B/GC-Net%20AWS%202005%20after%20raising%20tower.JPG",
                                    className="align-items-center",
                                    style={
                                        "display": "block",
                                        "margin-left": "auto",
                                        "margin-right": "auto",
                                        "width": "70%",
                                    },
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
                                    dbc.Button(
                                        "View processing scheme",
                                        href="https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing",
                                        color="light",
                                    ),
                                ],
                                color="dark",
                                outline=True,
                            ),
                            width=6,
                            className="align-self-center",
                        ),
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    dbc.Button(
                                        "Download data",
                                        href="https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing/tree/main/L1",
                                        color="light",
                                    ),
                                ],
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
