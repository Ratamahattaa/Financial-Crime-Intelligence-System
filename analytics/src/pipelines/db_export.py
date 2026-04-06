import pandas as pd
from sqlalchemy import create_engine

def get_engine():
    # dostosuj do swojej bazy
    return create_engine("postgresql://user:pass@localhost:5432/aml")

def write_transactions_scored(df: pd.DataFrame):
    engine = get_engine()
    df.to_sql("transactions_scored", engine, if_exists="replace", index=False)

def write_customer_risk(risk_df: pd.DataFrame):
    engine = get_engine()
    risk_df[["customer_id", "risk_score"]].to_sql(
        "customer_risk", engine, if_exists="replace", index=False
    )
