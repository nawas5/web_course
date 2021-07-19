import glob
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash.dependencies import Input, Output, State


import pandas as pd
import numpy as np

from initial_figures import initial_figure_simulation


tracking_file_list = glob.glob("data/*.json")
tracking_files = [w.replace("data\\", "") for w in tracking_file_list]
tracking_files = [s for s in tracking_files if "json" in s]

image_file = "assets/Pitch.png"

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO],
                meta_tags=[{
                    "name": "viewport", "content": "width=device-width, initial-scale=1"
                },
        ],
)
server = app.server

app.title = "PEERS"

app.layout = html.Div(
    children=[html.Div(
        children=[
            html.H1(children="PEERS", className="header-title"),
            html.P(children="Мониторинг персонала внутри помещений"
                   " и предотвращение несчастных случаев на производстве",
                   className="header-description",
                   ),
        ],
        className="header",
    ),
    html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(children="Tracking File", className="menu-title"),
                    # dbc.Select
                    dcc.Dropdown(
                        id="tracking-file",
                        options=[{"label": i, "value": i} for i in tracking_files],
                        value=None,
                        placeholder="Select a file for tracking",
                    ),
                ]
            ),
            html.Div(children=[
                    html.Div(children="Speed Motion", className="menu-title"),
                    daq.Slider(
                        id="speed-slider",
                        min=2.5,
                        max=5,
                        step=0.5,
                        value=3,
                        handleLabel={"showCurrentValue": True,"label": "VALUE"},
                    ),
                ]
            ),
            html.Div(children=[
                html.Div(children="Start Visualization", className="menu-title"),
                dbc.Button("Submit", id="submit-button", className="button-2"),
                ]
            ),
        ],
        className="menu",
        ),
    html.Div(children=[
        html.Div(
            children=dcc.Graph(
                id="game-simulation",
                animate=True,
                figure=initial_figure_simulation(image_file),
                config={
                    "modeBarButtonsToAdd": [
                        "drawline",
                        "drawopenpath",
                        "drawcircle",
                        "drawrect",
                        "eraseshape",
                    ],
                    "modeBarButtonsToRemove": [
                        "toggleSpikelines",
                        "pan2d",
                        "autoScale2d",
                        "resetScale2d",
                    ],
                    "displayModeBar":False
                },
            ),
            className="card",
            )
        ],
        className="wrapper",
        ),
    ]
)


@app.callback(
    Output("game-simulation", "figure"),
    Input("submit-button", "n_clicks"),
    State("speed-slider", "value"),
    State("tracking-file", "value"),
    prevent_initial_call=True,
)

def game_simulation_graph(n_clicks, speed, filename):

    speed_adjusted = speed * 100
    game_speed = 600 - speed_adjusted
    fig = fig_from_json("data/" + filename)
    fig.update_layout(margin=dict(l=0, r=20, b=0, t=0))
    # загрузка - для отображения
    fig.update_layout(newshape=dict(line_color="#2ca6cf"))

    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = game_speed

    fig.update_yaxes(scaleanchor="x", scaleratio=0.70)
    fig.update_layout(
        updatamenus=[
            dict(
                type="buttons",
                showactive=False,
                y=-0.10,
                x=-0.08,
                xanchor="left",
                yanchor="buttom",
            )
        ]
    )

    fig.update_layout(autosize=True)
    fig.update_layout(modebar=dict(bgcolor="rgba(0, 0, 0, 0)", orientation="v"))
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    fig.update_layout(legend=dict(font=dict(family="Roboto", size=10, color="grey")))

    fig.update_layout(
        template="plotly_dark",
        xaxis=dict(showgrid=False, showticklabels=False),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    fig["layout"]["template"]["data"]["scatter"][0]["marker"]["line"]["color"] = "white"
    fig["layout"]["template"]["data"]["scatter"][0]["marker"]["opacity"] = 0.9
    return fig

if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1")