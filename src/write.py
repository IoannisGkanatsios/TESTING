from pathlib import Path

import pandas as pd


def write(df: pd.DataFrame, path: Path):
    df.to_csv(path)
