import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from helpers.data_parsing.data_reader import dwelling_type_period_2021
from helpers.data_parsing.tables import image_locations, table_locations, colors
from helpers.introduction.table2 import get_table2


def get_figure4(cd: int) -> str:
    label = get_table2([cd])
    title = f"Housing stock in 2021 by Period of Construction - [{label.at[label.index[0], 'Geography']}]"
    file_name = "figure4"

    dwelling_data = dwelling_type_period_2021.xs('total by structural type', axis=1, level=1)
    # get percentage built
    total = "total by construction period"
    periods = list(dwelling_data.columns)
    periods.remove(total)

    percentages = dwelling_data.loc[cd, periods]/dwelling_data.at[cd, total]
    # I want it to have cumulative percentage
    for index in range(1,len(percentages)):
        percentages.iat[index] = percentages.iat[index] + percentages.iat[index-1]
    df = pd.concat([dwelling_data.loc[cd, periods], percentages], axis=1)
    df.columns = ["Number of Dwellings", "Cumulative Percentage"]

    df.to_csv(table_locations + file_name + ".csv")

    # Rename the " to " to "-\n" to save space, also the or to keep things similar
    df.index = [x.replace(" to ", "-<br>") for x in list(df.index)]
    df.index = [x.replace(" or", " or<br>") for x in list(df.index)]

    trace1 = go.Bar(
        x=df.index,
        y=df["Number of Dwellings"],
        name="Number of Dwellings",
        marker=dict(
            color='green'
        )
    )
    trace2 = go.Scatter(
        x=df.index,
        y=df["Cumulative Percentage"],
        name="Cumulative Percentage",
        yaxis='y2',
        marker=dict(
            color='grey'
        )
    )

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(trace1)
    fig.add_trace(trace2, secondary_y=True)
    fig['layout'].update(title=title, xaxis=dict(
        tickangle=0,
    ))

    # fig.update_yaxes(rangemode="tozero")
    fig.update_layout(legend=dict(
        orientation="h",
    ))
    fig.write_image(image_locations + file_name + ".png", width=1000, height=500)
    return file_name + ".png"