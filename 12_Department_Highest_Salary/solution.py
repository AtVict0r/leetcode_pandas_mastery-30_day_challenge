import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    joined_data = employee.merge(department, left_on='departmentId', right_on='id')
    # return joined_data
    grouped_data = joined_data.groupby('name_y').apply(lambda x: x[x['salary'] == x['salary'].max()])
    return grouped_data[['name_y', 'name_x', 'salary']].rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})