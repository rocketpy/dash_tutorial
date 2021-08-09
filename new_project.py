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

# country iso with counts
col_label = "country_code"
col_values = "count"

v = df[col_label].value_counts()
new = pd.DataFrame({col_label: v.index,
                    col_values: v.values
                   })

# create the map with the ‘country_iso’ and ‘count’ columns
