from pathlib import Path

import pandas as pd

DATA_PATH = Path("/home/ioannis/IOANNIS/my_projects/TESTING")

insurance_path = DATA_PATH / "raw" / "GeoData_Scientist_Interview_Task.xlsx"


def load(insurance_path: str) -> pd.DataFrame:
    """seresdsdr"""
    df_property = pd.read_excel(insurance_path, sheet_name="property_data")
    return df_property


def write(df: pd.DataFrame  , path: )-> None:
    df.to_csv(path)
