"""
This is a boilerplate pipeline
generated using Kedro 0.18.5
"""
from typing import List, Union

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline
from sklearn.linear_model import  LinearRegression
from .nodes import split_data, train_model, make_predictions, report_mean_error


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["ipa_lifecycle_data", "params:dataparameters"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="model",
                name="train_model",
            ),
            node(
                func=make_predictions,
                inputs=["X_test", "model"],
                outputs="y_pred",
                name="make_predictions",
            ),
            node(
                func=report_mean_error,
                inputs=["y_pred", "y_test"],
                outputs=None,
                name="report_mean_error",
            ),

        ]
    )
