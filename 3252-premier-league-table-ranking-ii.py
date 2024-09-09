import pandas as pd

def calculate_team_tiers(ts: pd.DataFrame) -> pd.DataFrame:

    def get_tier(pct):
        if pct <= ceil(ts.position.quantile(.33)):
            tier = 1
        elif pct <= ceil(ts.position.quantile(.66)):
            tier = 2
        else:
            tier = 3
        return 'Tier %s' % tier


    ts['points'] = 3 * ts.wins + ts.draws
    ts['position'] = ts.points.rank(method='min', ascending=False)
    ts['tier'] = ts.position.apply(get_tier)

    return ts.sort_values(['points', 'team_name'], ascending=[0, 1]).iloc[:, [1,6,7,8]]
