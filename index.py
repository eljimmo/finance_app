# Import necessary libraries 
from sys import set_asyncgen_hooks
from dash import html, dcc
from django.http import HttpResponse

from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app

# Connect to your app pages
from pages import analytics, archive, dashboard, list


# Connect the navbar to the index
from components import navbar

# define the navbar
nav = navbar.Navbar()

# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav, 
    html.Div(id='page-content', children=[]), 
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/analytics':
        return analytics.layout
    if pathname == '/applefinance':
        return applefinance.layout
    if pathname == '/dashboard':
        return dashboard.layout
    if pathname == '/list':
        return list.layout
 
    else:
        return "404 Page Error! Please choose a link"

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)
