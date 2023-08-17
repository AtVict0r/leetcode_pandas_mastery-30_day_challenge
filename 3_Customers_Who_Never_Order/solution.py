import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge the 'customers' and 'orders' DataFrames on 'id' and 'CustomerId' columns respectively
    merged_df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    
    # Filter out the customers who never made any orders (i.e., their 'CustomerId' is NaN after the merge)
    customers_never_ordered = merged_df[merged_df['customerId'].isnull()]
    
    # Return a new DataFrame containing the names of customers who never made any orders
    return customers_never_ordered[['name']].rename(columns={'name': 'Customers'})