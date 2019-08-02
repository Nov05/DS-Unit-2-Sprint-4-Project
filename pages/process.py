import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            **Data Source**  
            SiP Dataset https://github.com/Derek-Jones/SiP_dataset  
            **GitHub Repository**  
            https://github.com/nov05/DS-Unit-2-Sprint-4-Project  

            """
        ),

    ],
)

layout = dbc.Row([column1])