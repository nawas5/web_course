import glob
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output, State

from fig_generator import fig_from_json
from initial_figures import initial_figure_simulator


# Create list of tracking json files available to select from via a pulldown menu

tracking_file_list = glob.glob("data/*.json")
tracking_files = [w.replace("data\\", "") for w in tracking_file_list]
tracking_files = [s for s in tracking_files if "json" in s]


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"},],
)

server = app.server

simulator_controls = [
    dbc.FormGroup(
        [
            dbc.Label("Tracking File:"),
            dbc.Select(
                id="tracking-file",
                options=[{"label": i, "value": i} for i in tracking_files],
                value=None,
                placeholder="Select a file for tracking",
            ),
        ]
    ),
    dbc.Card(
        daq.Knob(
            id="speed-knob",
            label="Playback Speed",
            value=2.5,
            max=5,
            color={"default": "#3598DC"},
            size=100,
        )
    ),
    dbc.Button("Submit", className="mr-2", id="submit-button", color="info"),
]

# Configure main app layout
app.layout = dbc.Container(
    fluid=True,
    children=[
        html.Header([html.H1("Match Analysis Tool")]),
        html.Br(),
        dbc.Row(
            {
                dbc.Card(simulator_controls),
                dbc.Col(
                    dbc.Card(
                        children=[
                            dcc.Loading(
                                id="loading-icon7",
                                children=[
                                    dcc.Graph(
                                        id="game-simulation",
                                        animate=True,
                                        figure=initial_figure_simulator(),
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
                                        },
                                    )
                                ],
                                type="default",
                            )
                        ]
                    ),
                ),
            },
            form=True,
            no_gutters=False,
        ),
    ],
)


# Callback for animated game simulation graph
@app.callback(
    Output("game-simulation", "figure"),
    Input("submit-button", "n_clicks"),
    State("speed-knob", "value"),
    State("tracking-file", "value"),
    prevent_initial_call=True,
)
def game_simulation_graph(n_clicks, speed, filename):
    speed_adjusted = speed * 100
    game_speed = 600 - speed_adjusted
    fig = fig_from_json("data/" + filename)
    fig.update_layout(margin=dict(l=0, r=20, b=0, t=0))
    fig.update_layout(newshape=dict(line_color="#009BFF"))
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = game_speed
    fig.update_yaxes(scaleanchor="x", scaleratio=0.70)
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                y=-0.10,
                x=-0.08,
                xanchor="left",
                yanchor="bottom",
            )
        ]
    )
    fig.update_layout(autosize=True)
    fig.update_layout(modebar=dict(bgcolor="rgba(0, 0, 0, 0)", orientation="v"))
    # Disable zoom. It just distorts and is not fine-tunable
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    fig.update_layout(legend=dict(font=dict(family="Arial", size=10, color="grey")))
    # Sets background to be transparent
    fig.update_layout(
        template="plotly_dark",
        xaxis=dict(showgrid=False, showticklabels=False),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    fig["layout"]["template"]["data"]["scatter"][0]["marker"]["line"]["color"] = "white"
    fig["layout"]["template"]["data"]["scatter"][0]["marker"]["opacity"] = 0.9
    return fig


if __name__ == "__main__":
    app.run_server(debug=False)
