import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go # plotly4.0.0
import pandas as pd

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smallersize screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            #### Software projects usually take longer than estimated...

            It is hard to estimate software project efforts. Change of requirements, unexpected technical difficulties, suddenly found defeats, developers having different experience and performance levels... all bring great uncertainties to the projects.
            
            &nbsp;
            
            #### How could effort estimation be improved?

            This app uses an effort estimation model built from a software company's historical data to improve manuel estimation.

            """
        ), # ╰(○'◡'○)╮
        dcc.Link(dbc.Button('Click on Me ╰(o\'◡\'o)╮', color='primary'), href='/predictions')
    ],
    md=4,
)

# e.g.
# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

path = "assets/hist_data.csv"
hist_data = pd.read_csv(path, index_col=0).values
group_labels = ['Hours Actual (log)', 'Hours Estimated (log)']
fig = ff.create_distplot(hist_data, group_labels, bin_size=0.1, show_rug=False)
fig.update_layout(
    title=go.layout.Title(text="Software Development Effort Distribution", xref="paper", x=0),
    margin=dict(l=1,r=1,t=30,b=1),  
    legend=dict(x=.65, y=.95),
    xaxis=go.layout.XAxis(
        tickmode = 'array',
        tickvals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        ticktext = ['Hours', 'e<br>(2.72 hours)', 'e^2<br>(7.39 hours)', 
                    'e^3<br>(20.09 hours)', 'e^4<br>(54.60 hours)', 'e^5<br>(148.41 hours)', 
                    'e^6<br>(403.43 hours)', 'e^7<br>(1096.63 hours)', 'e^8<br>(2980.96 hours)', 
                    'e^9<br>(8103.08 hours)']),
)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])