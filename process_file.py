import pandas as pd
import time


def process(filepath):
    """ Randomally delete 90% of rows"""
    df = pd.read_csv(filepath)
    df = df.drop(df[df.columns[0]].sample(frac=0.9).index)
    time.sleep(1)
    return df
