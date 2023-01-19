from dash import html
import dash_bootstrap_components as dbc


def create_navbar():
    """
    This function creates a navigation bar.

    Returns:
        navigation_bar (object): The navigation bar.
    """
    navigation_bar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [dbc.Col(dbc.NavbarBrand("GEUS | GCNVis", className="ms-2"))],
                        align="start",
                        className="g-0",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.Nav(
                    [
                        dbc.NavLink("ABOUT", href="/about"),
                    ],
                    class_name="ms-auto",
                ),
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src="assets/logos/logo_github.png", height="30px"
                                )
                            )
                        ],
                        align="end",
                        className="g-0",
                    ),
                    title="View code",
                    href="https://github.com/silorepos/gcnvis",
                    style={"textDecoration": "none"},
                ),
            ],
            fluid=True,
        ),
        color="dark",
        dark=True,
        className="mb-4",
    )

    return navigation_bar
