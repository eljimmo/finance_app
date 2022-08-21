import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
from data_generator import DataGenerator
from logger import Logger


dash.register_page(__name__)



#data technicals into variables

trade_sticker = 'AAPL'
start_date="2017-01-01"
end_date="2022-07-23"
logger = Logger('./logs', '_')

data_gen= DataGenerator(trade_sticker, start_date,end_date,'./logs','./outputs','original',False,logger)


#our data being held in variables


dff = data_gen.generate_data()

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
data = yf.Ticker("AAPL")

###first figure 
fig = px.scatter(df, x='Date', y='AAPL.High', range_x=['2015-12-01', '2016-01-15'],
                 title="Hide Weekend and Holiday Gaps with rangebreaks")


fig.update_xaxes(
    rangebreaks=[
        dict(bounds=["sat", "mon"]), #hide weekends
        dict(values=["2015-12-25", "2016-01-01"])  # hide Christmas and New Year's
])

#second figure
fig2 = px.line(df, x='Date', y='AAPL.High', title='Time Series with Rangeslider')

fig2.update_xaxes(rangeslider_visible=True)

#third figure

fig3 = px.histogram(df, x="Date", y="AAPL.Close", histfunc="avg", title="Histogram on Date Axes")

fig3.update_traces(xbins_size="M1")

fig3.update_xaxes(showgrid=True, ticklabelmode="period", dtick="M1", tickformat="%b\n%Y")

fig3.update_layout(bargap=0.1)
fig3.add_trace(go.Scatter(mode="markers", x=df["Date"], y=df["AAPL.Close"], name="daily"))

layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    
    html.Div(children='''
        Summarizing Time-series Data with Rangesliders.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig2
        ),

    
    html.Div(children='''
        Summarizing Time-series Data with Histograms.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig3
        ),

        ])
