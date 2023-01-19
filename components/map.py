import json
import dash_leaflet as dl
from dash import html
from dash_extensions.javascript import assign
from config.constants import raster_tiles


def get_info(feature=None):
    header = [html.H4("Station Details")]
    if not feature:
        return header + [html.P("Hover over a station")]
    return header + [
        "Name: " + (feature["properties"]["name"]),
        html.Br(),
        "Elevation: " + (feature["properties"]["elevation"] + " m"),
        html.Br(),
        "Activation date: " + (feature["properties"]["startdate"]),
    ]


with open("metadata/station_info.json") as json_file:
    json_data = json.load(json_file)

info = html.Div(
    children=get_info(),
    id="info",
    className="info",
    style={"position": "absolute", "top": "10px", "right": "10px", "z-index": "1000"},
)

point_to_layer = assign(
    """function(feature, latlng, context){
    // Check if station is selected
    const selected = context.props.hideout.includes(feature.properties.name);
    // Display selected station in green
    if(selected){return L.circleMarker(latlng, {color: 'green'});}
    // Display non-selected stations in grey
    return L.circleMarker(latlng, {color: 'grey'});
}"""
)


def create_minimap():
    """
    This function creates a Leaflet minimap with the following components:
        - dl.TileLayer: Uses the URL specified by raster_tiles to display tiles on the map.
        - dl.GeoJSON: Displays GeoJSON data from the json_data file.
        - dl.Map: Renders the minimap, using the dl.TileLayer and dl.GeoJSON components.
    Returns:
        dl_minimap (object): The minimap.
    """
    dl_minimap = html.Div(
        dl.Map(
            children=[
                info,
                dl.TileLayer(url=raster_tiles, minZoom=3),
                dl.GeoJSON(
                    data=json_data,
                    options=dict(pointToLayer=point_to_layer),
                    hideout=["Summit"],
                    # zoomToBounds=True,
                    id="geojson",
                ),
            ],
            style={"width": "100%", "height": "42vh"},
            zoomControl=True,
            attributionControl=False,
            id="map",
            zoom=3,
            zoomDelta=0.5,
            zoomSnap=0.5,
            center=[76, -42],
        ),
        className="g-0",
    )

    return dl_minimap


minimap = create_minimap()
