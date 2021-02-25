"""
name: Michael Moore
date: 2/20/21
Program: Steam_Store.py

This program uses pandas built in functions to prep data set for visualization.
"""
import pandas as pd

df = pd.read_csv('steam.csv', sep=',', index_col="publisher")
new_df = pd.DataFrame(df.groupby('publisher')['positive_ratings'].sum())
df_rows_delete = new_df[new_df['positive_ratings'] < 50].index
df_rows_delete = list(df_rows_delete)
df = df.drop(df_rows_delete)
df = df.sort_values(by= "positive_ratings", ascending=False)
print(df['name'])
print(df.describe())
df = df.drop(['appid'], axis=1)
df['publisher'] = df.index
df = df.set_index('owners')
print(df)
df = df.drop('0-20000')
df['owners'] = df.index
df = df.set_index('publisher')
print(df)


new_df = pd.DataFrame(df, columns=['owners'],)


