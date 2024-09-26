import pandas as pd
import numpy as np


def load(path: str) -> pd.DataFrame:
    return pd.read_csv(path, index_col=0)
