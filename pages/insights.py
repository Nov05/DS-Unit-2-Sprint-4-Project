import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go # plotly-4.0.0
import pandas as pd

from app import app

url = "https://raw.githubusercontent.com/Nov05/DS-Unit-2-Sprint-4-Project/master/assets/hours_category2.csv"
path = "assets/hours_category2.csv"
df = pd.read_csv(path)
df = df.round(2)

fig = go.Figure(data=[go.Table(
    header=dict(values=['Category', 'Sub Cat', 'Ttl Task', 
                         'Est Sum', 'Actl Sum', 
                         'Est Max', 'Actl Max',
                         'Est Min', 'Actl Min'],
                align='left'),
    cells=dict(values=[df['Category'], 
                       df['SubCategory'], 
                       df['TaskNumber'], 
                       df['HoursEstimateSum'],
                       df['HoursActualSum'],
                       df['HoursEstimateMax'],
                       df['HoursActualMax'],
                       df['HoursEstimateMin'],
                       df['HoursActualMin'],
                      ],
               align='left')),
])
fig.update_layout(margin=dict(l=1,r=1,t=1,b=1),
                 )

block1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Insights
            #### Category
            There are 3 task categories. Most tasks are development.

            | Category    |  Total Tasks | 
            |-------------|--------------| 
            | Development |  8220        | 
            | Management  |  2105        | 
            | Operational |  1974        | 
            
            ![alt text]('assets/hours_per_subcategory.png')
            """
        ),
    ],
    md=4,
)

block2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

block3 = dbc.Col(
    [
        dcc.Markdown(
            """
            #### test
            """
        ),
    ],
    md=4,
)

block4 = dbc.Col(
    [
        dcc.Markdown(
            """
             
            """
        ),        
    ]
)

layout = dbc.Col(
    [
        dbc.Row([block1, block2]),
        dbc.Row([block3, block4])
    ]
)