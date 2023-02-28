import logging
from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd


def modify_locale(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """

    Returns:

    """
    df[col] = df[col].str.replace('$', '')
    return df


def reduce_databricks_cols(df: pd.DataFrame, databricks: Dict) -> pd.DataFrame:
    for client in databricks['clients']:
        df.loc[df['client'] == client, databricks["cols"]] /= 2
    return df


def reduce_database_cols(df: pd.DataFrame, database: Dict) -> pd.DataFrame:
    for client in database['clients']:
        df.loc[df['client'] == client, database["cols"]] /= 2
    return df


def join_all_cost(df_1: pd.DataFrame, df_2: pd.DataFrame, df_3: pd.DataFrame) -> pd.DataFrame:
    df_merged = pd.merge(pd.merge(df_1, df_2, on=['client', 'month'], how='inner'), df_3, on=['client', 'month'],
                         how='inner')

    df_merged['total_ipa_cost'] = df_merged['database_cost'] + df_merged['databricks_cost'] + df_merged['lc_cost']
    df_merged = df_merged[df_merged.columns.difference(['database_cost', 'databricks_cost', 'lc_cost', 'client'])]
    return df_merged

# def join_all_cost(df: List[pd.DataFrame]) -> pd.DataFrame:
#     df_merged = pd.merge(pd.merge(df[0], df[1], on=['client', 'month'], how='inner'), df[2], on=['client', 'month'],
#                          how='inner')

# return df_merged
