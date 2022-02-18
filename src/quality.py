def check_nulls(df):
    assert df.isnull().sum().sum() == 0