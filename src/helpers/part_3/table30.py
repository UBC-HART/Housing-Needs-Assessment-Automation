import pandas as pd

import report_input
from helpers.data_parsing.tables import projections
from helpers.part_3.table31 import get_table31


def get_table30(geo_code: int):
    beds = [1, 2, 3, 4, 5]
    income_lv_list = ['20% or under', '21% to 50%', '51% to 80%', '81% to 120%', '121% or more']
    row = projections.loc[geo_code, :]
    df = pd.DataFrame(columns=income_lv_list, index=beds)
    for bed in beds:
        for i in income_lv_list:
            df.loc[bed, i] = row.loc[f"2031 Projected bedroom need {bed} bed {i}"]
    # Get totals for row and columns
    df['Total'] = df.sum(axis=1)
    df.loc['Total'] = df.sum()
    # Rename columns and rows
    df = df.rename(
        columns={'20% or under': 'veryLow', '21% to 50%': 'low', '51% to 80%': 'moderate',
                 '81% to 120%': 'median', '121% or more': 'high'})
    df = df.rename(
        index={1: "1", 2: "2", 3: "3", 4: "4", 5: "5+"}
    )
    df = df.astype(int)
    return df


get_table30(report_input.community_cd)