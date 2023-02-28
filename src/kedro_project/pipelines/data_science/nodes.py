import logging
from typing import Any, Dict, Tuple
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


def split_data(
    data: pd.DataFrame, dataparameters: Dict
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Splits data into features and target training and test sets.

    Args:
        data: Data containing features and target.
        dataparameters: Parameters defined in parameters.yml.
    Returns:
        Split data.
    """

    data_train = data.sample(
        frac=dataparameters["train_fraction"], random_state=dataparameters["random_state"]
    )
    data_test = data.drop(data_train.index)

    X_train = data_train.drop(columns=dataparameters["target_column"])
    X_test = data_test.drop(columns=dataparameters["target_column"])
    y_train = data_train[dataparameters["target_column"]]
    y_test = data_test[dataparameters["target_column"]]

    return X_train, X_test, y_train, y_test


def train_model(X_train: np.ndarray, y_train: np.ndarray) -> LinearRegression:
    linear_regression = LinearRegression()
    linear_regression.fit(X_train, y_train)
    return linear_regression


def make_predictions(X_test: pd.DataFrame, model: LinearRegression) -> pd.Series:
    y_pred = model.predict(X_test)
    return y_pred


def report_mean_error(y_pred: pd.Series, y_test: pd.Series):
    """Calculates and logs the error.

    Args:
        y_pred: Predicted target.
        y_test: True target.
    """
    mean_error = (np.abs(y_pred - y_test)).sum() / len(y_test)
    logger = logging.getLogger(__name__)
    logger.info("Model has error of %.3f on test data.", mean_error)