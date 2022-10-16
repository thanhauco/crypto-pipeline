def agg(df):
    return df.groupby('coin').mean()