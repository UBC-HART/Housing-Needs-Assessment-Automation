import pandas as pd

import report_input
from helpers.data_parsing.table_import import AMHI_2016
from helpers.part_1.part_2_community_names import single_community_name

info_list = ["AMHI", "very low income", "low income", "moderate income", "median income", "high income"]
def get_table46(geo_code):
    df: pd.Series = AMHI_2016.loc[geo_code, info_list]
    # rename index
    df = df.rename(index={
        "very low income": "Very Low",
        "low income": "Low",
        "moderate income": "Moderate",
        "median income": "Median",
        "high income": "High"
    })
    df.loc["AMHI"] = int(df.loc["AMHI"])
    df.loc["AMHI"] = "${:,.0f}".format(df.loc["AMHI"])

    # df.loc["Very Low"] = "< " + df.loc["Very Low"]

    df.name = single_community_name(geo_code)
    return df.to_frame()



get_table46(report_input.community_cd)
