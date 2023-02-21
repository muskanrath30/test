import re

import numpy as np
import pandas as pd


def _get_first_cabin(row):
    try:
        return row.split()[0]
    except Exception:
        return np.nan


def _get_title(passenger) -> str:
    line = passenger
    if re.search("Mrs", line):
        return "Mrs"
    elif re.search("Mr", line):
        return "Mr"
    elif re.search("Miss", line):
        return "Miss"
    elif re.search("Master", line):
        return "Master"
    else:
        return "Other"


def clean_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe_copy = dataframe.copy()

    dataframe_copy = dataframe_copy.replace("?", np.nan)
    dataframe_copy["cabin"] = dataframe_copy["cabin"].apply(_get_first_cabin)
    dataframe_copy["title"] = dataframe_copy["name"].apply(_get_title)
    dataframe_copy["fare"] = dataframe_copy["fare"].astype("float")
    dataframe_copy["age"] = dataframe_copy["age"].astype("float")
    dataframe_copy.drop(
        labels=["name", "ticket", "boat", "body", "home.dest"], axis=1, inplace=True
    )

    return dataframe_copy
