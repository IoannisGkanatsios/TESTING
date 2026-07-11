from os import path

import pandas as pd


def write(df: pd.DataFrame, path: path):
    df.to_csv(path)
