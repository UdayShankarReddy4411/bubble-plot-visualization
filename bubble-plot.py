import pandas as pd
import plotly.express as px
# Load Indian dataset
df = pd.read_csv("C:/Users/udays/OneDrive/Desktop/Bubble-data-visualization/data.csv")

# Create bubble plot map
fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    size="population",
    color="state",          # use state instead of country
    hover_name="city",
    hover_data={"population": ":,d"},
    projection="natural earth"
)

# Zoom into India
fig.update_geos(
    scope="asia",           # show Asia
    center={"lat": 22, "lon": 80},  # roughly center India
    projection_scale=5      # zoom in (bigger = closer)
)

fig.update_traces(marker=dict(opacity=0.7, line=dict(width=0.5, color="white")))
fig.update_layout(
    title="Bubble Plot Map of Major Indian Cities by Population",
    margin=dict(l=10, r=10, t=40, b=10)
)
fig.write_html("index.html", include_plotlyjs="cdn")
fig.show()
