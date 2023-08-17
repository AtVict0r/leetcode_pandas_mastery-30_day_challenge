import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Create a mask to filter employees based on the conditions for getting a bonus
    mask = (employees['employee_id'] % 2 != 0) & ~employees['name'].str.startswith('M')
    
    # Step 2: Calculate the bonus for each employee based on the mask and store it in a new column
    employees['bonus'] = employees['salary'].where(mask, 0)
    
    # Step 3: Return a new DataFrame containing only the 'employee_id' and 'bonus' columns, ordered by 'employee_id'
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')