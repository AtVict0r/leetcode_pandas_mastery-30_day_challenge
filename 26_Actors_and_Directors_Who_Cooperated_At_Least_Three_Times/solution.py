import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    result = actor_director.groupby(['director_id', 'actor_id'])['timestamp'].count().reset_index()
    mask = result['timestamp'] >= 3
    return result[mask][['actor_id', 'director_id']]