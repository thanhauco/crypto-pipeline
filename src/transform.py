import pandas as pd
def clean_data(data):
    df = pd.DataFrame(data)
    return df.dropna()