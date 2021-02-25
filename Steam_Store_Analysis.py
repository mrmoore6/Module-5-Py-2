"""
Name: Michael Moore
Date: 2/24/21
Program: Steam_Store_Analysis.py

This program we get a lot more in depth with and narrow are results with pandas.
"""

import pandas as pd
from Steam_Store import df

new_df = pd.DataFrame(df, columns=['owners', 'positive_ratings', 'negative_ratings'])

df_sum = pd.DataFrame(new_df.groupby('owners').sum())

print(df_sum)


df_sum['positive_percentile'] = df_sum['positive_ratings'] / (df_sum['negative_ratings'] + df_sum['positive_ratings'])
df_sum['negative_percentile'] = df_sum['negative_ratings'] / (df_sum['positive_ratings'] + df_sum['negative_ratings'])
df_sort1 = df_sum.sort_values(by="positive_percentile", ascending=False)
df_sort2 = df_sum.sort_values(by="negative_percentile", ascending=False)
pd.options.display.float_format = '{:.0%}'.format
print(df_sort1['positive_percentile'])
print(df_sort2['negative_percentile'])

df = df.reset_index()

newer_df = pd.DataFrame(df, columns=['publisher', 'positive_ratings', 'negative_ratings'])
newer_df = newer_df.groupby("publisher").filter(lambda x: len(x) >= 5)
new_df_sum = pd.DataFrame(newer_df.groupby('publisher').sum())
print(new_df_sum)
new_df_sum['positive_percentile'] = new_df_sum['positive_ratings'] / (new_df_sum['negative_ratings'] + new_df_sum['positive_ratings'])
new_df_sum['negative_percentile'] = new_df_sum['negative_ratings'] / (new_df_sum['positive_ratings'] + new_df_sum['negative_ratings'])
new_df_sum = new_df_sum.sort_values(by="positive_percentile", ascending=False)
new_df_sum = new_df_sum.sort_values(by="negative_percentile", ascending=False)
pd.options.display.float_format = '{:.0%}'.format
print(new_df_sum.sort_values(by="positive_percentile", ascending=False).head())
print(new_df_sum.sort_values(by="negative_percentile", ascending=False).head())

df_rows_delete = new_df_sum[new_df_sum['positive_ratings'] < 1000].index
df_rows_delete = list(df_rows_delete)
new_df_sum = new_df_sum.drop(df_rows_delete)

print(new_df_sum.sort_values(by="positive_percentile", ascending=False).head())





#new_df_sum = new_df_sum.drop(new_df_sum['positive_ratings'] > 1000)

"""df_per = df['owners'].value_counts(normalize=True) * 100
sorted(df_per)
print('\n', df_per)"""

