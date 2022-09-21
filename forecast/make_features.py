import pandas as pd


def create_time_based_features(
    df: pd.DataFrame, date_label: str
) -> pd.DataFrame:
    """
    Create features for model training.

    :param df: df
    :param date_label: name of the date column
    """
    df["hour"] = df[date_label].dt.hour

    df["date"] = df[date_label].dt.date
    df["dayofweek"] = df[date_label].dt.dayofweek
    df["quarter"] = df[date_label].dt.quarter
    df["month"] = df[date_label].dt.month
    df["year"] = df[date_label].dt.year
    df["dayofyear"] = df[date_label].dt.dayofyear
    df["dayofmonth"] = df[date_label].dt.day
    df["weekofyear"] = df[date_label].dt.weekofyear

    return df


def make_features_for_predict(df: pd.DataFrame) -> pd.DataFrame:
    """
    :param df: df
    """
    ...
