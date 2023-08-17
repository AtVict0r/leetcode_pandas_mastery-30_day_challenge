import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Define a regular expression pattern for valid emails
    pattern = r'^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$'
    
    # Step 2: Use the .str.match() method to apply the regex pattern on the 'mail' column
    valid_users = users['mail'].str.match(pattern)
    
    # Step 3: Return the final result after dropping the temporary column
    return users[valid_users].reset_index(drop=True)