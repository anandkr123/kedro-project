"""
This is a boilerplate pipeline
generated using Kedro 0.18.5
"""
from typing import List, Union

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline
from .nodes import modify_locale, reduce_database_cols, reduce_databricks_cols,join_all_cost


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=modify_locale,
                inputs=["lc_data", "params:col"],
                outputs="lc_process_data",
                name="dollar_to_euro",
            ),
            node(
                func=reduce_databricks_cols,
                inputs=["databricks_data", "params:databricks"],
                outputs="databricks_process_data",
                name="reduce_databricks_cols",
            ),
            node(
                func=reduce_database_cols,
                inputs=["database_data", "params:database"],
                outputs="database_process_data",
                name="reduce_database_cols",
            ),
            node(
                func=join_all_cost,
                inputs=['lc_process_data', 'database_process_data', 'databricks_process_data'],
                outputs="ipa_lifecycle_data",
                name="join_all_cost",
            ),
        ]
    )
