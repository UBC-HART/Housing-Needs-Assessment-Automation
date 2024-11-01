import pandas as pd

from helpers.data_parsing.table_names import save_location

comprehensive_2006 = pd.read_pickle(save_location+"comprehensive_2006.pkl")
comprehensive_2011 = pd.read_pickle(save_location+"comprehensive_2011.pkl")
comprehensive_2016 = pd.read_pickle(save_location+"comprehensive_2016.pkl")
comprehensive_2021 = pd.read_pickle(save_location+"comprehensive_2021.pkl")

PHM_2006 = pd.read_pickle(save_location+"PHM_2006.pkl")
HART_2006 = pd.read_pickle(save_location+"HART_2006.pkl")
dwelling_type_bedrooms_2021 = pd.read_pickle(save_location+"dwelling_type_bedrooms_2021.pkl")
dwelling_type_period_2021 = pd.read_pickle(save_location+"dwelling_type_period_2021.pkl")

consolidated_2006 = pd.read_pickle(save_location+"consolidated_2006.pkl")
consolidated_2016 = pd.read_pickle(save_location+"consolidated_2016.pkl")
consolidated_2021 = pd.read_pickle(save_location+"consolidated_2021.pkl")

AMHI_2006 = pd.read_pickle(save_location+"AMHI_2006.pkl")
AMHI_2016 = pd.read_pickle(save_location+"AMHI_2016.pkl")
AMHI_2021 = pd.read_pickle(save_location+"AMHI_2021.pkl")

tenure_2016 = pd.read_pickle(save_location+"tenure_2016.pkl")
tenure_2021 = pd.read_pickle(save_location+"tenure_2021.pkl")

income_bedroom_2021 = pd.read_pickle(save_location+"income_bedroom_2021.pkl")