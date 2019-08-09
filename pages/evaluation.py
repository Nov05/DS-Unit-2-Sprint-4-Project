import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go # plotly-4.0.0
import pandas as pd

from app import app

#######################################################
# Plotly Figures
#######################################################
url = "https://raw.githubusercontent.com/Nov05/DS-Unit-2-Sprint-4-Project/master/assets/hours_predict.csv"
path = "assets/hours_predict.csv"
hours = pd.read_csv(path, index_col=0)

def plotly_errors(hoursactual, hoursestimate, title):
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=hoursactual, 
                           y=hoursestimate,
                           mode='markers', 
                           hovertemplate="Actual: %{x:.2f}<br>Esitmated: %{y:.2f}",
                           name='effort hours (log)',
                           marker=dict(size=6, opacity=0.6,
                                       color=hoursestimate-hoursactual,
                                       colorscale='RdBu',
                                       line=dict(width=0.5, color='DarkSlateGrey'),
                                       showscale=True,
                                       reversescale=True,
                                       colorbar=dict(title='Error (log)',
                                                     thickness=5,
                                                     outlinewidth=0,),
                                      ),
                          )
               )
  fig.add_trace(go.Scatter(x=[0,8], y=[0,8],
                           mode='lines',
                           line=dict(color='DarkSlateGrey', width=2, dash='dash'),
                           name='perfect estimation'))
  fig.update_layout(title=title,
                    autosize=False, width=550, height=500,
                    margin=dict(l=1,r=1,t=30,b=1),
                    legend=dict(x=.05, y=.95),
                    xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Actual Hours (log)")),
                    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Estimated Hours (log)")),
                   )
  return fig

# Plotly Scatterplot takes long time to render...
samples = hours.sort_values(by='HoursActual').sample(int(len(hours)/30))
fig1 = plotly_errors(samples['HoursActual'], samples['HoursEstimate'], "Manuel Estimation Samples (1/30)")
fig2 = plotly_errors(samples['HoursActual'], samples['HoursPredict'], "Model Prediction Samples (1/30)")
fig3 = plotly_errors(samples['HoursActual'], samples['HoursPredict2'], "Model Prediction (without Manuel Estimation) Samples (1/30)")

#######################################################
# Web Page Content
#######################################################
header = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Evaluation  
            HoursEstimate-HoursActual RMSE: 0.752  
            Model RMSE (with manuel estimation): 0.637   
            Model RMSE (without manuel estimation): 1.002  
            """
        ),
    ],
    width=12,
)

block1 = dbc.Col(
    [
        html.Div([   
            dcc.Graph(figure=fig1),
        ], style={'width': '10%'}),
    ],
    md=4,
)

block2 = dbc.Col(
    [
        dcc.Graph(figure=fig2),
    ],
    md=4,
)

block3 = dbc.Col(
    [
        dcc.Graph(figure=fig3),
    ],
    md=4,
)

blankrow = dbc.Col([dcc.Markdown("""&nbsp;"""),],md=4,)

#######################################################
# Web Page Layout
#######################################################
layout = dbc.Col([
    dbc.Row(header),
    dbc.Row(blankrow),
    dbc.Row([block1, block2, block3]), 
#     dbc.Row(blankrow),
#    dbc.Row([block3, block4]),
#    dbc.Row(blankrow),
])