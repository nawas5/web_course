import requests
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import plotly.io as poi

poi.renderers.default = 'browser'

response = requests.get('http://asterank.com/api/kepler?query={}&limit=2000')

df = pd.json_normalize(response.json())

#print(df.head())

fig = px.scatter(df, x='TPLANET', y='A')
#fig.show()

# делаем слайдер - интерактивность графика
# интересно а сюда можно ли Bootstrap включать
# как делать активным или реактивным график
# несколько фильтров могут работать на один график

rplanet_slader = dcc.RangeSlider(
    id='range-slider',
    min=min(df['RPLANET']),
    max=max(df['RPLANET']),
    marks={5: '5', 10: '10', 20: '20'},
    step=1,
    value=[5,50]
)
# инициализация dash - для этого создавали файл с именем dash

app = dash.Dash(__name__)

# внешний вид html - наполнение html.Div
# пишется на React и наверное лучше сразу всё делать на реакте
# children - наполнитель - как раз список, т.е. квадратные скобки []
# для графика dcc

app.layout = html.Div(
    children=[
        html.H1('Hello Dash'),
        html.Div('Exoplanet chart'),
        dcc.Graph(figure=fig),
    ]
)
# в конце не обязательно ставить запятую - можно и без неё

if __name__ == '__main__':
    app.run_server(debug=True)