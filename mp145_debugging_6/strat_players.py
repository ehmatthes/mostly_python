from datetime import datetime

import plotly.express as px

import player_data

# Generate plot.
fig = px.timeline(
    player_data.df,
    x_start="start",
    x_end="end",
    y="name",
)

# Customize plot.
fig.update_yaxes(autorange="reversed")

fig.update_layout(title="Fender Strat players")
fig.update_layout(yaxis_title=None)

fig.update_traces(marker_color='SteelBlue')
fig.update_traces(marker_opacity=0.6)

fig.show()
