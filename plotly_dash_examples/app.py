import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc

import requests
import pandas as pd

import plotly.express as px

""" READ DATA """

response = requests.get('http://asterank.com/api/kepler?query={}&limit=2000')
df = pd.json_normalize(response.json())
# удаляем экстремальные точки руками - оставляем только где период больше нуля
df = df[df['PER'] > 0]

"""CATEGORY"""
bins = [0, 0.8, 1.1, 50]
names = ['small', 'similar','bigger']
df['StarSize'] = pd.cut(df['RSTAR'], bins, labels=names)

options = []
for k in names:
    options.append({'label': k, 'value': k})

"""SLIDER"""

rplanet_selector = dcc.RangeSlider(
    id='range-slider',
    min=min(df['RPLANET']),
    max=max(df['RPLANET']),
    marks={(a * 5): str(a * 5) for a in range(1,11)},
    step=1,
    value=[5,50]
)

star_size_selector = dcc.Dropdown(
    id='star-selector',
    # нужно передавать в виде списка
    options=options,
    value=['small','similar','bigger'],
    multi=True
)

"""APP"""

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.FLATLY])

# bootstrap - для колонков и строк, ширина, отступы и так далее
# интересно проще ли его задавать отдельно?
# Row - контенты для строк

"""LAYOUT"""

app.layout = html.Div(
    children=[
        html.H1('Hello Dash'),
        html.Div('Select planet main semi-axis range'),
        html.Div(rplanet_selector,
                 style={
                     'width': '400px',
                     'margin-bottom': '40px',
                     'margin-top': '40px'
                 }),
        html.Div('Star Size'),
        html.Div(star_size_selector,
                 style={
                     'width': '400px',
                     'margin-bottom': '40px',
                     'margin-top': '40px'
                 }),
        html.Div('Planet Temperature ~ Distance from the Star'),
        dcc.Graph(id='dist-temp-chart')
    ],
    style={
        'margin-left': '80px',
        'margin-right': '80px'
    }
)


"""CALLBACKS"""

@app.callback(
    Output(component_id='dist-temp-chart', component_property='figure'),
    [Input(component_id='range-slider', component_property='value'),
     Input(component_id='star-selector', component_property='value')]
)

def update_dist_temp_chart(radius_range, star_size):
    chart_data = df[
        (df['RPLANET'] > radius_range[0]) &
        (df['RPLANET'] < radius_range[1]) &
        (df['StarSize'].isin(star_size))
    ]

    fig = px.scatter(chart_data, x='TPLANET', y='A', color='StarSize')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)