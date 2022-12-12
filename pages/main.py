import copy
import dash_bootstrap_components as dbc
import json
import pandas as pd
import dash_leaflet as dl
import plotly.express as px
from dash_extensions.javascript import assign
from components import settings
from components import graphs
from dash import callback, html, Input, Output, clientside_callback
from config.constants import options_air_temp, options_humidity, options_radiation, options_wind_speed, \
    options_wind_direction, options_all, raster_tiles

# Load data
df_daily = pd.read_parquet("data/df_daily.gzip")
df_hourly = pd.read_parquet("data/df_daily.gzip")

seasons = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring",
           6: "Summer", 7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn",
           11: "Autumn", 12: "Winter"}

df_daily["season"] = df_daily.index.month.map(seasons)

# Data settings
dd_and_slider = settings.create_dd_and_slider()
filters = settings.create_filters()

# Interactive graphs
tabs = dbc.Tabs(
    [
        dbc.Tab(graphs.time_series, label="Time Series", active_label_style={"font-weight": "800", "color": "#00AEF9"}),
        dbc.Tab(graphs.scatter_plots,
                label="Scatter Plots", active_label_style={"font-weight": "800", "color": "#00AEF9"}),
        dbc.Tab(graphs.violin_plots, label="Violin Plots",
                active_label_style={"font-weight": "800", "color": "#00AEF9"}),
        dbc.Tab(graphs.uncertainty_test, label="Uncertainty (test)",
                active_label_style={"font-weight": "800", "color": "#00AEF9"}),
    ]
)


# Minimap
def get_info(feature=None):
    header = [html.H4("Station Details")]
    if not feature:
        return header + [html.P("Hover over a station")]
    return header + ["Name: " + (feature["properties"]["name"]), html.Br(),
                     "Elevation: " + (feature["properties"]["elevation"] + " m"), html.Br(),
                     "Activation date: " + (feature["properties"]["startdate"])]


with open("metadata/station_info.json") as json_file:
    json_data = json.load(json_file)

info = html.Div(children=get_info(), id="info", className="info",
                style={"position": "absolute", "top": "10px", "right": "10px", "z-index": "1000"})

point_to_layer = assign("""function(feature, latlng, context){
    // Check if station is selected
    const selected = context.props.hideout.includes(feature.properties.name);
    // Display selected station in green
    if(selected){return L.circleMarker(latlng, {color: 'green'});}
    // Display non-selected stations in grey
    return L.circleMarker(latlng, {color: 'grey'});
}""")


def create_minimap():
    """
    This function creates a Leaflet minimap with the following components:
        - dl.TileLayer: Uses the URL specified by raster_tiles to display tiles on the map.
        - dl.GeoJSON: Displays GeoJSON data from the json_data file.
        - dl.Map: Renders the minimap, using the dl.TileLayer and dl.GeoJSON components.
    Returns:
        dl_minimap (object): The minimap.
    """
    dl_minimap = dbc.Card(
        dbc.CardBody(
            dl.Map(children=[
                info,
                dl.TileLayer(url=raster_tiles, minZoom=3),
                dl.GeoJSON(data=json_data,
                           options=dict(pointToLayer=point_to_layer),
                           hideout=["Summit"],
                           # zoomToBounds=True,
                           id="geojson"),
            ], style={'width': '100%', 'height': '50vh'}, zoomControl=False, attributionControl=False, id="map", zoom=3,
                center=[76, -42]),
        ),
        className="mt-1",
    )

    return dl_minimap


minimap = create_minimap()

# Main layout
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.CardHeader("Data Settings"),
                        dd_and_slider,
                        filters,
                        minimap
                    ],
                    width=4,
                ),
                dbc.Col(
                    [
                        tabs,
                    ],
                    width=8,
                ),
            ]
        ),
    ],
    fluid=True,
)


# Callback 1
@callback(
    [Output('dropdown', 'options'),
     Output('dropdown', 'value')],
    Input('filter-2', 'value'))
def dropdown_options(value):
    options_and_values = {
        'Temperature': {
            'options': options_air_temp,
            'value': ["TA1", "TA2", "TA2m", "TA3", "TA4"],
        },
        'Radiation': {
            'options': options_radiation,
            'value': ["ISWR", "OSWR", "NR"],
        },
        'Wind Speed': {
            'options': options_wind_speed,
            'value': ["VW1", "VW2", "VW10m"],
        },
        'Wind Direction': {
            'options': options_wind_direction,
            'value': ["DW1", "DW2"],
        },
        'Humidity': {
            'options': options_humidity,
            'value': ["RH1", "RH2", "RH2m"],
        },
        'Customize': {
            'options': options_all,
            'value': [],
        },
    }

    options_and_values_for_filter = options_and_values.get(value, {
        'options': options_all,
        'value': [],
    })

    return options_and_values_for_filter['options'], options_and_values_for_filter['value']


# Callback 2
@callback(
    Output("time-series", "figure"),
    Input("dropdown", "value"),
    Input("station-dd", "value"),
    Input("slider", "value"),
    Input("filter-1", "value"),
    Input("filter-2", "value"),
)
def update_line_chart(dropdown, station, yrs, value2, value):
    dff = copy.deepcopy(df_daily if value2 == "Daily" else df_hourly)
    dff = dff[dff.year.astype(int).between(yrs[0], yrs[1])]

    if station is not None:
        dff = dff.query("station_name == @station")

    fig = px.line(
        dff,
        x=dff.index,
        y=dropdown,
        title=f"{value} ({station})",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    fig.update_traces(mode="lines", hovertemplate=None)
    fig.update_layout(
        hovermode="x",
        modebar_add=["v1hovermode"],
        modebar_remove=["pan", "toggleSpikelines", "toImage", "resetScale2d", 'autoScale2d',
                        'zoom2d', "zoomIn2d", "zoomOut2d"],
        modebar_orientation="h",
        margin=dict(l=25, r=25, t=40, b=20)
    )
    fig.update_layout(xaxis_rangeslider_visible=True)
    fig.update_layout(legend_title="", xaxis_title="Date", yaxis_title=None)
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ))
    fig.update_xaxes(showgrid=False, showspikes=True, spikethickness=2, spikedash="dot", spikecolor="#999999",
                     spikemode="across")

    if value == "Temperature":
        fig.update_yaxes(ticksuffix=" °C")
    elif value == "Radiation":
        fig.update_yaxes(ticksuffix=" W/m^2")
    elif value == "Wind Speed":
        fig.update_yaxes(ticksuffix=" m/s")
    elif value == "Wind Direction":
        fig.update_yaxes(ticksuffix=" °")
    elif value == "Humidity":
        fig.update_yaxes(ticksuffix=" %")
    else:
        fig.update_yaxes(ticksuffix=" n/a")

    return fig


# Callback 3
@callback(
    Output('scatter-plot', 'figure'),
    Input("station-dd", "value"),
    Input("slider", "value"),
    Input('scatter-plot-dd-1', 'value'),
    Input('scatter-plot-dd-2', 'value'),
    Input('scatter-plot-dd-3', 'value'),
    Input('filter-1', 'value'),
)
def update_scatter(station, yrs, drop1, drop2, drop3, value):
    dff = copy.deepcopy(df_daily if value == "Daily" else df_hourly)
    dff = dff[dff.year.astype(int).between(yrs[0], yrs[1])]

    if station is not None:
        dff = dff.query("station_name == @station")

    trendline = "ols" if drop3 == "OLS trendline" else "lowess"
    fig = px.scatter(
        data_frame=dff,
        x=drop1,
        y=drop2,
        title="{} vs. {} ({})".format(drop1, drop2, station),
        trendline=trendline,
        trendline_color_override="black",
    )
    fig.update_layout(
        modebar_remove=["pan", "toggleSpikelines", "toImage", "resetScale2d", 'autoScale2d',
                        'zoom2d', "zoomIn2d", "zoomOut2d", "lasso2d", "select2d"],
        modebar_orientation="h",
        margin=dict(l=25, r=25, t=40, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )
    fig.data[0].name = 'Observations'  # noqa
    fig.data[0].showlegend = True  # noqa
    fig.data[1].name = "Trendline"  # noqa
    fig.data[1].showlegend = True  # noqa

    return fig


# Callback 4
@callback(
    Output('scatter-matrix', 'figure'),
    Input("station-dd", "value"),
    Input("slider", "value"),
    Input('scatter-matrix-dd', 'value'),
    Input('filter-1', 'value'),
)
def update_matrix(station, yrs, drop, value):
    dff = copy.deepcopy(df_daily if value == "Daily" else df_hourly)
    dff = dff[dff.year.astype(int).between(yrs[0], yrs[1])]

    if station is not None:
        dff = dff.query("station_name == @station")

    fig = px.scatter_matrix(
        dff,
        dimensions=drop,
        title="Scatter Matrix ({})".format(station),
    )
    fig.update_layout(
        modebar_remove=["pan", "toggleSpikelines", "toImage", "resetScale2d", 'autoScale2d',
                        "zoomIn2d", "zoomOut2d"],
        modebar_orientation="h",
        margin=dict(l=25, r=25, t=40, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )
    fig.update_traces(diagonal_visible=False)

    return fig


# Callback 5
@callback(
    Output("ridge-chart", "figure"),
    Input("dropdown", "value"),
    Input("station-dd", "value"),
    Input("slider", "value"),
    Input("filter-1", "value"),
    Input("filter-2", "value"),
)
def update_ridge_chart(dropdown, station, yrs, value, value2):
    dff = copy.deepcopy(df_daily if value == "Daily" else df_hourly)
    dff = dff[dff.year.astype(int).between(yrs[0], yrs[1])]

    if station is not None:
        dff = dff.query("station_name == @station")

    fig = px.violin(
        dff,
        x=dropdown,
        y="month",
        color="month",
        points="suspectedoutliers",
        category_orders={
            "month": ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']},
        title=f"{value2} ({station})",
        orientation='h',
    )

    fig.update_layout(
        modebar_remove=["pan", "toggleSpikelines", "toImage", "resetScale2d", 'autoScale2d',
                        'zoom2d', "zoomIn2d", "zoomOut2d"],
        modebar_orientation="h",
        margin=dict(l=25, r=25, t=40, b=20)
    )

    fig.update_layout(xaxis_zeroline=False)
    fig.update_layout(legend_title="", xaxis_title=f"{value2}", yaxis_title=None)
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.03,
        xanchor="center",
        x=0.5
    ))
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True)
    fig.update_xaxes(showspikes=False)
    fig.update_yaxes(showspikes=False)
    fig.update_traces(meanline_visible=True)
    fig.update_traces(side='positive', width=3)

    if value == "Temperature":
        fig.update_xaxes(ticksuffix=" °C")
    elif value == "Radiation":
        fig.update_xaxes(ticksuffix=" W/m^2")
    elif value == "Wind Speed":
        fig.update_xaxes(ticksuffix=" m/s")
    elif value == "Wind Direction":
        fig.update_xaxes(ticksuffix=" °")
    elif value == "Humidity":
        fig.update_xaxes(ticksuffix=" %")
    else:
        fig.update_xaxes(ticksuffix=" n/a")

    return fig


# Callback 6
@callback(
    Output("violin-plot", "figure"),
    Input("dropdown", "value"),
    Input("station-dd", "value"),
    Input("slider", "value"),
    Input("filter-1", "value"),
    Input("filter-2", "value"),
)
def update_ridge_chart(dropdown, station, yrs, value, value2):
    dff = copy.deepcopy(df_daily if value == "Daily" else df_hourly)
    dff = dff[dff.year.astype(int).between(yrs[0], yrs[1])]

    if station is not None:
        dff = dff.query("station_name == @station")

    fig = px.violin(
        dff,
        x="season",
        y=dropdown,
        color="season",
        box=True,
        points="suspectedoutliers",
        category_orders={"month": ['Spring', 'Summer', 'Autumn', 'Winter']},
        title=f"{value2} ({station})",
    )

    fig.update_layout(
        hovermode="x unified",
        modebar_remove=["pan", "toggleSpikelines", "toImage", "resetScale2d", 'autoScale2d',
                        'zoom2d', "zoomIn2d", "zoomOut2d"],
        modebar_orientation="v",
        margin=dict(l=25, r=25, t=40, b=20)
    )

    fig.update_xaxes(showspikes=False)
    fig.update_yaxes(showspikes=False)
    fig.update_layout(xaxis_zeroline=False)
    fig.update_layout(legend_title="", xaxis_title="Season", yaxis_title=None)
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ))
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True)
    fig.update_traces(meanline_visible=True)

    if value2 == "Temperature":
        fig.update_yaxes(ticksuffix=" °C")
    elif value2 == "Radiation":
        fig.update_yaxes(ticksuffix=" W/m^2")
    elif value2 == "Wind Speed":
        fig.update_yaxes(ticksuffix=" m/s")
    elif value2 == "Wind Direction":
        fig.update_yaxes(ticksuffix=" °")
    elif value2 == "Humidity":
        fig.update_yaxes(ticksuffix=" %")
    else:
        fig.update_yaxes(ticksuffix=" n/a")

    return fig


# Callback 7
@callback(
    Output("null-chart", "figure"),
    Input("station-dd", "value"),
    Input("slider", "value"),
    Input("filter-1", "value")
)
def update_null_chart(station, yrs, value):
    dff = copy.deepcopy(df_daily if value == "Daily" else df_hourly)
    dff = dff[dff.year.astype(int).between(yrs[0], yrs[1])]

    dff = dff.drop(columns=['month', 'season', 'year'])

    if station is not None:
        dff = dff.query("station_name == @station")

    dff_null = dff.isnull().sum().to_frame()
    dff_null = dff_null.rename(columns={0: 'Null'})
    dff_not_null = dff.notna().sum().to_frame()
    dff_not_null = dff_not_null.rename(columns={0: 'Not Null'})
    dff_null_count = pd.concat([dff_null, dff_not_null], ignore_index=False, axis=1).reset_index()
    dff_null_count = dff_null_count.rename(columns={'index': 'Category'})

    fig = px.bar(
        dff_null_count,
        x="Category",
        y=['Not Null', 'Null'],
        barmode='relative',
        title=f"Null Values ({station}) {yrs}")
    # fig.update_xaxes(categoryorder='total descending')
    fig.update_traces(hovertemplate=None)
    fig.update_layout(
        hovermode="x unified",
        modebar_remove=["pan", "toggleSpikelines", "toImage", "resetScale2d", 'autoScale2d',
                        'zoom2d', "zoomIn2d", "zoomOut2d"],
        modebar_orientation="h",
        margin=dict(l=25, r=25, t=40, b=20)
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True)
    fig.update_xaxes(showspikes=False)
    fig.update_yaxes(showspikes=False)
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ))
    fig.update_layout(legend_title="", xaxis_title="Category", yaxis_title="Count")

    return fig


# Callback 8
@callback(Output("info", "children"), [Input("geojson", "hover_feature")])
def info_hover(feature):
    return get_info(feature)


# Callback 9 (testing the performance of a clientside callback)
clientside_callback("function(x){return x;}", Output("geojson", "hideout"), Input("station-dd", "value"))
