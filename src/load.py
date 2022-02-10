from sqlalchemy import create_engine
def load_db(df, uri):
    engine = create_engine(uri)
    df.to_sql('prices', engine, if_exists='append')