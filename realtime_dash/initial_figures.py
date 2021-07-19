import plotly.express as px
import os

# Create initial placeholder figure for game simulator
def initial_figure_simulator():
    # fig = px.scatter(x=[0, 0, 105, 105], y=[69, -2, 69, -2])
    fig = px.scatter(x=[0, 0, 1, 1], y=[0, 1, 0, 1])
    fig.update_layout(xaxis=dict(range=[0, 1]))
    fig.update_layout(yaxis=dict(range=[0, 1]))
    fig.update_traces(marker=dict(color="white", size=6))

    # Remove side color scale and hide zero and gridlines
    fig.update_layout(
        coloraxis_showscale=False,
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
        autosize=True
        # width=900,
        # height=600
    )

    # Disable axis ticks and labels
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text="")
    fig.update_layout(margin=dict(l=80, r=80, b=10, t=20))
    fig.update_layout(modebar=dict(bgcolor="rgba(0, 0, 0, 0)"))
    image_file = "assets/Pitch.png"
    image_path = os.path.join(os.getcwd(), image_file)

    # Import and use pre-fabricated football pitch image
    from PIL import Image

    img = Image.open(image_path)

    fig.add_layout_image(
        dict(
            source=img,
            xref="x",
            yref="y",
            x=0,
            y=1,
            sizex=1,
            sizey=1,
            sizing="stretch",
            opacity=0.7,
            layer="below",
        )
    )

    fig.update_yaxes(scaleanchor="x", scaleratio=0.70)

    fig.update_layout(autosize=True)

    fig.update_layout(
        template="plotly_dark",
        xaxis=dict(showgrid=False, showticklabels=False),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    return fig
