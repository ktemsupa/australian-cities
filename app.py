#!/usr/bin/env python
# coding: utf-8

# In[7]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


# In[8]:


########### Define your variables
cities=['Adelaide', 'Sydney', 'Gold Coast', 'Brisbane']
ibu_values=[40, 100, 65, 10]
abv_values=[6.5, 2.0, 4.0, 8.0]
color1='lightgreen'
color2='lightblue'
mytitle='City Comparison'
tabtitle='city!'
myheading='City Visit Analysis'
label1='IBU'
label2='ABV'
githublink='https://github.com/ktemsupa/flying-dog-beers'
sourceurl='https://www.australia.com/en-us'


# In[11]:


########### Set up the chart
bitterness = go.Bar(
    x=cities,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=cities,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

cities_data = [bitterness, alcohol]
cities_layout = go.Layout(
    barmode='group',
    title = mytitle
)

cities_fig = go.Figure(data=cities_data, layout=cities_layout)


# In[12]:


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle


# In[ ]:


########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=cities_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()


# In[ ]:
