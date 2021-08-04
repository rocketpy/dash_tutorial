import numpy as np
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
#  Need Install: Dash, Pycountry, Plotly, and Pandas


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

df = pd.read_csv('file_name.csv', encoding="ISO-8859-1")


