# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


#  navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("analytics", href="/analytics")),
                dbc.NavItem(dbc.NavLink("applefinance", href="/applefinance")),
                dbc.NavItem(dbc.NavLink("dashboard", href="/dashboard")),
                dbc.NavItem(dbc.NavLink("list", href="/list")),
            ] ,
            brand="Multipage Dash App",
            brand_href="/analytics",
            color="dark",
            dark=True,
        ), 
    ])

    return layout
