import pandas as pd

def calculate_team_standings(ts: pd.DataFrame) -> pd.DataFrame:
    ts['points'] = 3 * ts.wins + ts.draws
    ts['position'] = ts.points.rank(method='min', ascending=False)

    return ts.sort_values(['points', 'team_name'], ascending=[0, 1]).iloc[:, [0,1,6,7]]
