from typing import Dict

import pandas as pd
from helpers.data_parsing.table_import import consolidated_2006, consolidated_2016, consolidated_2021, \
    AMHI_2006, AMHI_2016, AMHI_2021

incomes = ["very low income", "low income", "moderate income", "median income", "high income", "total by income"]


def get_table4(geo_code: int) -> pd.DataFrame:
    df = pd.DataFrame(
        index=incomes,
        columns=[2006, 2016, 2021]
    )

    tables: Dict[int, pd.DataFrame] = {
        2006: consolidated_2006,
        2016: consolidated_2016,
        2021: consolidated_2021
    }
    for year in df.columns:
        # Get any total from level 0 of dataframe
        labels = list(tables[year].columns.levels[0])
        total = next((value for value in labels if 'total' in value.lower()), None)
        # All totals do the same damn thing, please only keep one in the future
        data: pd.Series = tables[year].loc[geo_code, (total, "total by household size", incomes, "total by CHN")]
        data.index = data.index.get_level_values(2)
        df.loc[:, year] = data
    # Add totals
    # totals = df.sum().to_frame().T
    # df = pd.concat([df, totals])
    # Calculate % changes between 2006 and 2016, then 2016 to 2021 as new columns
    df["change"] = (df[2016] - df[2006]) / df[2006] * 100
    df["change1"] = (df[2021] - df[2016]) / df[2016] * 100
    # Make populations integers
    df.iloc[:, :3] = df.iloc[:, :3].astype(int)

    # Make percentages actually percent
    df.iloc[:, 3:] = (df.iloc[:, 3:]).astype(float).round().astype(int).astype(str) + "%"
    return df


AMHI_tables = {
    2006: AMHI_2006,
    2016: AMHI_2016,
    2021: AMHI_2021
}


def get_AMHI(geo_code: int) -> Dict[int, str]:
    out = {
        2006: "",
        2016: "",
        2021: ""
    }
    for year in AMHI_tables.keys():
        try:
            out[year] = '{:,}'.format(int(AMHI_tables[year].loc[geo_code, "AMHI"]))
        except KeyError:
            out[year] = "N/A"

    return out


# get_table4(3511)