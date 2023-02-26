import logging
from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd


def modify_locale(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """

    Returns:

    """
    df[col] = df[col].str.replace('$', '€')
    return df


def reduce_databricks_cols(df: pd.DataFrame, databricks: Dict) -> pd.DataFrame:

    for client in databricks['clients']:
        df.loc[df['client'] == client, databricks["cols"]] /= 2
    return df


def reduce_database_cols(df: pd.DataFrame, database: Dict) -> pd.DataFrame:

    for client in database['clients']:
        df.loc[df['client'] == client, database["cols"]] /= 2
    return df
