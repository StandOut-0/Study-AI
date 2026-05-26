import os
import math
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path


def test_csv_load(csv_path):
    df = pd.read_csv(csv_path)
    return df

def get_numeric_columns(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    print("Numeric columns:", numeric_cols)
    return numeric_cols

def test_dataframe_hist_subplot(df):
    numeric_cols = get_numeric_columns(df)
    col_count = len(numeric_cols)
    fig, axes = plt.subplots(col_count, 1, figsize=(6, 4 * col_count))
    if col_count == 1:
        axes = [axes]
    for ax, col in zip(axes, numeric_cols):
        sns.histplot(df[col], ax=ax, bins=10)
        ax.set_title(f'{col} Histogram')
        ax.set_xlabel(col)
        ax.set_ylabel('Count')
    plt.tight_layout()
    plt.show()



def test_dataframe_boxplot_subplot(df):
    numeric_cols = get_numeric_columns(df)
    col_count = len(numeric_cols)
    fig, axes = plt.subplots(1, col_count, figsize=(5 * col_count, 4))
    if col_count == 1:
        axes = [axes]
    for ax, col in zip(axes, numeric_cols):
        sns.boxplot(df[col], ax=ax)
        ax.set_title(f'{col} Boxplot')
        ax.set_xlabel(col)
        ax.set_ylabel('Value')
    plt.tight_layout()
    plt.show()

def test_dataframe_groupby_subplot(df, category_col):
    numeric_cols = get_numeric_columns(df)
    grouped = df.groupby(category_col)[numeric_cols].mean()
    # grouped.plot(kind='bar', figsize=(8, 6))

    grouped.plot(
        kind='bar',
        figsize=(8, 6),
        secondary_y='salary'
    )
    
    plt.show()




if __name__ == "__main__":
    # df = test_csv_load("./sample.csv")
    # df = test_csv_load("../sample.csv")

    base_dir = Path(__file__).parent.parent
    print(base_dir/'sample.csv')
    df = test_csv_load(base_dir/'sample.csv')
    print(df)
    # get_numeric_columns(df)
    # test_dataframe_hist_subplot(df)
    # test_dataframe_boxplot_subplot(df)
    test_dataframe_groupby_subplot(df,'age_category')