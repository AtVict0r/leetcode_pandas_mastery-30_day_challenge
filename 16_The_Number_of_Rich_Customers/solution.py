import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    mask = store['amount'] > 500
    rich_count = store[mask][['customer_id']].nunique()
    return pd.DataFrame({'rich_count': rich_count})