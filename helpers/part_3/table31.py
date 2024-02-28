import pandas as pd

from helpers.context_helpers import get_community_name
from helpers.data_parsing.table_import import income_bedroom_2021


def get_table31(geo_code: int):
    df: pd.DataFrame = income_bedroom_2021.loc[geo_code, :].unstack()
    df = df[["very low income", "low income", "moderate income", "median income", "high income"]]
    df['Total'] = df.sum(axis=1)
    df.loc['Total'] = df.sum()
    # Rename columns and rows
    df = df.rename(
        columns={"very low income": 'veryLow', 'low income': 'low', 'moderate income': 'moderate',
                 'median income': 'median', 'high income': 'high'})
    df = df.rename(
        index={"5": "5+"}
    )
    df = df.astype(int)
    return df


get_table31(1)