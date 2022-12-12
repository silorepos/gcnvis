import dash_bootstrap_components as dbc
from dash import dcc, html
from config.constants import options_air_temp, station_list, years


def create_station_dd():
    """
    This function creates a station dropdown.

    Returns:
        station_dd (object): The station dropdown.
    """
    station_dd = dbc.Card(
        dbc.CardBody(
            [
                html.H6("Select station:"),
                dcc.Dropdown(
                    id="station-dd",
                    options=[dict(value=s["name"], label=s["name"]) for s in station_list],
                    value="Summit",
                    clearable=False,
                    maxHeight=500,
                )
            ]
        )
    )

    return station_dd


def create_slider():
    """
    This function creates a year range slider.

    Returns:
        slider (object): The year range slider.
    """
    slider = dbc.Card(
        dbc.CardBody(
            [
                html.H6("Select year range:"),
                dcc.RangeSlider(
                    min=years[0],
                    max=years[-1],
                    step=1,
                    id="slider",
                    marks={year: str(year) for year in range(1990, 2023, 4)},
                    allowCross=False,
                    tooltip={"placement": "bottom", "always_visible": False},
                    value=[years[0], years[-1]],
                )
            ]
        )
    )

    return slider


def create_dd_and_slider():
    """
    This function creates a row containing the station dropdown and year range slider.

    Returns:
        station_dd_and_slider (object): The combined `station_dd_and_slider` object.
    """
    station_dd = create_station_dd()
    slider = create_slider()

    station_dd_and_slider = dbc.Row(
        [
            dbc.Col(station_dd, width=3),
            dbc.Col(slider, width=9),
        ],
        className="g-0",
    )

    return station_dd_and_slider


def create_filters():
    """
    This function creates a set of filters that can be used to filter the data in various ways.

    Returns:
        filter_set (object): A set of filters.
    """
    filter_set = dbc.Card(
        dbc.CardBody(
            [
                html.H6("Filter by:"),
                dbc.Checklist(
                    id='filter-1',
                    value='Daily',
                    inline=True,
                    switch=True,
                    options=[
                        {"label": "Daily data", "value": "Daily"},
                        {"label": "Hourly data (temporarily disabled)", "value": "Hourly", "disabled": True},
                    ],
                ),
                dbc.RadioItems(
                    id='filter-2',
                    value='Temperature',
                    inline=True,
                    options=[{'label': x, 'value': x}
                             for x in
                             ['Temperature', 'Radiation', 'Wind Speed', "Wind Direction", 'Humidity', "Customize"]]
                ),

                dcc.Dropdown(id='dropdown',
                             multi=True,
                             options=options_air_temp,
                             value=["TA1", "TA2", "TA2m", "TA3", "TA4"]),
            ]
        ),
    )

    return filter_set

# Call
# dd_and_slider = create_dd_and_slider()
# filters = create_filters()
