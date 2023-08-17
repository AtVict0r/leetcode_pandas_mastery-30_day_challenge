import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Create a mask to filter the rows where author_id is equal to viewer_id
    mask = views['author_id'] == views['viewer_id']
    
    # Use the mask to filter the DataFrame and get the rows where authors viewed their own articles
    result = views[mask]
    
    # Select only the 'author_id' column from the filtered DataFrame
    result = result[['author_id']]
    
    # Drop duplicates to count the number of distinct authors who viewed their own articles
    result = result.drop_duplicates()
    
    # Sort the result by 'author_id' in ascending order
    result = result.sort_values(by=['author_id'])
    
    # Rename the 'author_id' column to 'id' to match the desired output format
    # Return the final DataFrame containing the 'id' column with authors who viewed their own articles
    return result.rename(columns={'author_id': 'id'})