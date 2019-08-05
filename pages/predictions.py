import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
from joblib import load 
import sklearn
import numpy as np
import pandas as pd
from joblib import load

###############################################
# Load Pipeline
###############################################
url1 = "https://github.com/Nov05/DS-Unit-2-Sprint-4-Project/blob/master/assets/pipeline1.joblib"
path1 = "assets/pipeline1.joblib"
pipeline1 = load(path1) 

url2 = "https://github.com/Nov05/DS-Unit-2-Sprint-4-Project/blob/master/assets/pipeline2.joblib"
path2 = "assets/pipeline2.joblib"
pipeline2 = load(path2) 

###############################################
# Dash Input Options
###############################################
# Performance Level: 1-10 int
# Manuel Estimation Hours: 0-2500 float
# convert list to dictionary
list_cate = ['Development', 'Management', 'Operational']
list_sub_dev = ['Enhancement', 'Bug', 'Support', 'Release', 'Training', 
               'Testing', 'Business Specification', 'Conversion', 
               'Technical Specification', 'Research', 'Documentation', 'Third Party']
list_sub_mngt = ['Marketing', 'Management Meeting', 'General Documentation', 'Progress Meeting', 
                'Staff Management', 'Office Management', 'Project Management', 'Client Support', 
                'Board Meeting', 'Staff Recruitment']
list_sub_oprt = ['In House Support', 'Client Support', 'Consultancy', 'Documentation']

def list_to_opt(l):
  opt = []
  for i in l:
    opt.append({'label':i, 'value':i})
  return opt
opt_cate = list_to_opt(list_cate)
opt_sub_dev = list_to_opt(list_sub_dev)
opt_sub_mngt = list_to_opt(list_sub_mngt)
opt_sub_oprt = list_to_opt(list_sub_oprt)

#######################################################
# Web Page Content
#######################################################
# Notes:
# Element IDs: html.Div() have prefixes as "dropdown_", "slider_" for formatting
#              dcc.Input() etc. have prefixes as "input_", "output_" for IO values
#
# https://dash.plot.ly/dash-html-components
header = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Predictions
            Input `Category`,  `Sub-Category`,  `Project Breakdown Number`,  `Priority`,  `Developer Performance Level`,  and `Hours Manuelly Estimated`, `With/Without Manuel Estimation`, then click on the "Submit" button, to get effort hour estimated by the model.
            """
        ),
    ],
    width=12,
)

block1 = dbc.Col(
    [
        # Category Dropdown        
        html.Div([
            dcc.Markdown("""#### Task Category"""),
            dcc.Dropdown(id='input_cate', options=opt_cate, value=list_cate[0]), 
        ], style={'marginBottom':15}),
        
        # SubCategory Dropdowns
        html.Div([
            dcc.Markdown("""#### Task Sub-Category"""),
            html.Div([
                dcc.Dropdown(id='input_sub_dev', options=opt_sub_dev, value=list_sub_dev[0]),
            ], style={'display':'block'}, id='dropdown_sub_dev'),
            html.Div([
                dcc.Dropdown(id='input_sub_mngt', options=opt_sub_mngt, value=list_sub_mngt[0]),
            ], style={'display':'none'}, id='dropdown_sub_mngt'),
            html.Div([
                dcc.Dropdown(id='input_sub_oprt', options=opt_sub_oprt, value=list_sub_oprt[0]),
            ], style={'display':'none'}, id='dropdown_sub_oprt'),
        ], style={'marginBottom':15,}),
        
        # Project Breakdown Number Text Input
        html.Div([
            dcc.Markdown("""#### Project Breakdown Number"""),
            html.Div([
                dcc.Input(id='input_breakdown', type='text', inputMode='numeric', value=1),
            ], style={'display':'inline-block', 'marginRight':5,}),
            html.Div([
                dcc.Markdown("""Integer larger than 1"""),
            ], style={'display':'inline-block'}),
        ], style={'marginBottom':1, 'display':'block'}),
    ],
    md=4,
)

block2 = dbc.Col(
    [
        # Slidebar    
        html.Div([
            dcc.Markdown("""#### Task Priority"""),
            dcc.Slider(id='input_prior', min=1, max=10, value=5,
                       marks={i:str(i) for i in range(1,11)},)  
        ], style={'marginBottom':36, 'display':'block'}),
        
        # Sliderbar   
        html.Div([
            dcc.Markdown("""#### Developer Performance Level"""),
            dcc.Slider(id='input_perf', min=1, max=10, value=5,
                       marks={i:str(i) for i in range(1,11)},)  
        ], style={'marginBottom':36, 'display':'block'}),
        
        # Manuel Estimate Text Input
        html.Div([
            dcc.Markdown("""#### Hours Manuelly Estimated"""),
            html.Div([
                dcc.Input(id='input_hours', type='text', inputMode='numeric', value=10.0),
            ], style={'display':'inline-block', 'marginRight':5,}),
            html.Div([
                dcc.Markdown("""Float larger than 0"""),
            ], style={'display':'inline-block'}),
        ], style={'marginBottom':1, 'display':'block'}),
    ],
    md=4,
)

block3 = dbc.Col(
    [   # Submit button
        dcc.Markdown("""#### Prediction"""),
        html.Div([
            dbc.Button('Submit', color='primary', id='input_submit'),
        ],style={'marginBottom':15, 'display':'block'}),
        
        # estimation output
        html.Div([
            dcc.Markdown("""#### With Manuel Estimation"""),
            html.Div([
                dcc.Input(id='output_hours1', type='text', inputMode='numeric', value=0,
                          disabled=True, debounce=True),
            ], style={'display':'inline-block', 'marginRight':5,}),
        ], style={'marginBottom':15, 'display':'block'}),
        
        # estimation output
        html.Div([
            dcc.Markdown("""#### Without Manuel Estimation"""),
            html.Div([
                dcc.Input(id='output_hours2', type='text', inputMode='numeric', value=0,
                          disabled=True, debounce=True),
            ], style={'display':'inline-block', 'marginRight':5,}),
        ], style={'marginBottom':1, 'display':'block'}),
    ],
    md=4,
)

#######################################################
# Layout
#######################################################
layout = dbc.Col([
    dbc.Row(header),
    dbc.Row([block1, block2, block3]),
])

#######################################################
# Callbacks
#######################################################
# CallbackMultiple inputs or outputs - https://dash.plot.ly/getting-started-part-2
# Output(), Input(): component_id, component_property
@app.callback([Output('dropdown_sub_dev', 'style'),
               Output('dropdown_sub_mngt', 'style'),
               Output('dropdown_sub_oprt', 'style'),], 
              [Input('input_cate', 'value'),])
def cb_dropdown_sub(input_cate):
    # list_cate = ['Development', 'Management', 'Operational']
    if input_cate == list_cate[0]:
        return {'display':'block'}, {'display':'none'}, {'display':'none'}
    elif input_cate == list_cate[1]:
        return {'display':'none'}, {'display':'block'}, {'display':'none'}
    elif input_cate == list_cate[2]:
        return {'display':'none'}, {'display':'none'}, {'display':'block'}
    
@app.callback([Output('output_hours1', 'value'),
               Output('output_hours2', 'value'),],
              [Input('input_submit', 'n_clicks'),],
              [State('input_cate', 'value'),
               State('input_sub_dev', 'value'),
               State('input_sub_mngt', 'value'),
               State('input_sub_oprt', 'value'),
               State('input_breakdown', 'value'),
               State('input_prior', 'value'),
               State('input_perf', 'value'),
               State('input_hours', 'value'),])
def cb_predict(input_n_clicks, input_cate, input_sub_dev,
               input_sub_mngt, input_sub_oprt, input_breakdown,
               input_prior, input_perf, input_hours): 
    if input_n_clicks <= 0:
        return
    # list_cate = ['Development', 'Management', 'Operational']
    if input_cate == list_cate[0]:
        subcate = input_sub_dev
    elif input_cate == list_cate[1]:
        subcate = input_sub_mngt
    elif input_cate == list_cate[2]:    
        subcate = input_sub_oprt
    cols = ['Priority', 'Category', 'SubCategory', 'hoursestimatelog', 'breakdown', 'performancelevel']
    X1 = pd.DataFrame([[input_prior, input_cate, subcate, np.log1p(float(input_hours)), int(input_breakdown), input_perf]],
                     columns=cols)
    # Predict with manuel estimation
    y1 = pipeline1.predict(X1)
    X2 = X1.drop('hoursestimatelog', axis=1)
    # Predict without manuel estimation
    y2 = pipeline2.predict(X2)
    return np.expm1(y1).round(1)[0], np.expm1(y2).round(1)[0]
    
    
    
    
    
    