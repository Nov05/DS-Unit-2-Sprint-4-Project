import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go # plotly-4.0.0
import pandas as pd

from app import app

#######################################################
# Plotly Figure
#######################################################
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

#######################################################
# Web Page Content
#######################################################
url_img1 = "https://raw.githubusercontent.com/Nov05/DS-Unit-2-Sprint-4-Project/master/images/hours_per_subcategory.png?raw=true"
url_img2 = "https://github.com/Nov05/DS-Unit-2-Sprint-4-Project/blob/master/images/hours%20actual%20and%20estimated.png?raw=true"
url_img3 = "https://github.com/Nov05/DS-Unit-2-Sprint-4-Project/blob/master/images/hour%20estimation%20errors.png?raw=true"
url_img4 = "https://github.com/Nov05/DS-Unit-2-Sprint-4-Project/blob/master/images/days_to_complete_a_task.png?raw=true"

header = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Insights  
            The "Sip Effort Estimation" dataset contains data collected from over ten years of commercial development using Agile (10,100 unique task estimates made by 22 developers, under 20 project codes). The dataset consists of 2 CSV files.   
            1. The `Sip-task-info.csv` has 17 columns: 'TaskNumber', 'Summary', 'Priority', 'RaisedByID', 'AssignedToID', 'AuthorisedByID', 'StatusCode', 'ProjectCode', 'ProjectBreakdownCode', 'Category', 'SubCategory', 'HoursEstimate', 'HoursActual', 'DeveloperID', 'DeveloperHoursActual', 'TaskPerformance', 'DeveloperPerformance';   
            2. The `est-act-dates.csv` has 4 columns: 'TaskNumber', 'EstimateOn', 'StartedOn', 'CompletedOn'.  
            """
        ),
    ],
    width=12,
)

block1 = dbc.Col(
    [
        dcc.Markdown(
            """
            #### Category
            There are 3 task categories. Most tasks are development.

            | Category    |  Total Tasks | 
            |-------------|--------------| 
            | Development |  8220        | 
            | Management  |  2105        | 
            | Operational |  1974        | 
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
            #### Total Hours per Sub-Category
            Most of time were spent on `Enhancement`, `Bug` and `In-House Support`.
            """
        ),
    ],
    md=4,
)

block4 = dbc.Col(
    [
        html.Img(id='img1', src=url_img1, width="700px")      
    ]
)

block5 = dbc.Col(
    [
        dcc.Markdown(
            """
            #### Actual Hours vs. Estimated Hours
            The actual hours has a long tail, and the distribution is highly skewed.
            """
        ),
    ],
    md=4,
)

block6 = dbc.Col(
    [
        html.Img(id='img2', src=url_img2, width="700px")      
    ]
)

block7 = dbc.Col(
    [
        dcc.Markdown(
            """
            #### Days to Complete a Task
            Similar to Actual Hours, this distribution is highly skewed.
            """
        ),
    ],
    md=4,
)

block8 = dbc.Col(
    [
        html.Img(id='img4', src=url_img4, width="700px")      
    ]
)

block9 = dbc.Col(
    [
        dcc.Markdown(
            """
            #### Estimation Errors
            If `Estimation Error = Hours Estimated - Hours Actual`, from the distribution 
            we could see:   
            1. errors are approximately within range (-700, 2500) hours;  
            2. most estimation errors are within a few hours, but two long tails indicate that some error numbers are huge;  
            3. people tend to under estimate effort for complex tasks.   
            """
        ),
    ],
    md=4,
)

block10 = dbc.Col(
    [
        html.Img(id='img3', src=url_img3, width="700px")      
    ]
)

blankrow = dbc.Col(
    [
        dcc.Markdown(
            """
            &nbsp;
            """
        ),
    ],
    md=4,
)

#######################################################
# Web Page Layout
#######################################################
layout = dbc.Col(
    [
        dbc.Row(header),
        dbc.Row(blankrow),
        dbc.Row([block1, block2]), 
        dbc.Row(blankrow),
        dbc.Row([block3, block4]),
        dbc.Row(blankrow),
        dbc.Row([block5, block6]),
        dbc.Row(blankrow),
        dbc.Row([block7, block8]),
        dbc.Row(blankrow),
        dbc.Row([block9, block10]),
    ]
)