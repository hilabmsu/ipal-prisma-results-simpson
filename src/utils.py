from pathlib import Path
import config
import pandas as pd


DATA_PATH = Path(__file__).parent.parent / 'data' / 'processed' / 'ipal-survey-results.csv'
DROP_ROWS = [2]

def load_data():
    df = pd.read_csv(DATA_PATH)
    df = df.drop(DROP_ROWS)

    if len(df) == 0:
        raise ValueError("DataFrame is empty after dropping rows.")
    return df

def validate_columns(df, label):
    if df.empty:
        raise ValueError(f"No columns found for {label}")
