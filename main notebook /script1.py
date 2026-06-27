import pandas as pd
import numpy as np

# 1. Load the core datasets
matches = pd.read_csv('all_matches.csv')
elo = pd.read_csv('elo_ratings_wc2026.csv')

# 2. Filter for modern era matches to avoid ancient data noise
matches['date'] = pd.to_datetime(matches['date'])
matches = matches[matches['date'].dt.year >= 2000].copy()
matches['Year'] = matches['date'].dt.year

# 3. Create the multi-class Classification Target (0 = Away Win, 1 = Draw, 2 = Home Win)
conditions = [
    (matches['home_score'] > matches['away_score']),
    (matches['home_score'] == matches['away_score']),
    (matches['home_score'] < matches['away_score'])
]
choices = [2, 1, 0]
matches['Match_Outcome'] = np.select(conditions, choices, default=np.nan)

# 4. Standardize Country Names
name_mapping = {
    "USA": "United States",
    "Korea Republic": "South Korea",
    "IR Iran": "Iran",
    "Türkiye": "Turkey",
    "Côte d'Ivoire": "Ivory Coast"
}
matches['home_team'] = matches['home_team'].replace(name_mapping)
matches['away_team'] = matches['away_team'].replace(name_mapping)
elo['country'] = elo['country'].replace(name_mapping)

# 5. Extract Elo ratings by Year (Simplifying to the latest snapshot per year)
elo_subset = elo.sort_values('snapshot_date').drop_duplicates(subset=['year', 'country'], keep='last')

# 6. Merge Home Elo
elo_home = elo_subset[['year', 'country', 'rating']].rename(
    columns={'year': 'Year', 'country': 'home_team', 'rating': 'home_elo'}
)
matches = pd.merge(matches, elo_home, on=['Year', 'home_team'], how='inner')

# 7. Merge Away Elo
elo_away = elo_subset[['year', 'country', 'rating']].rename(
    columns={'year': 'Year', 'country': 'away_team', 'rating': 'away_elo'}
)
matches = pd.merge(matches, elo_away, on=['Year', 'away_team'], how='inner')

# 8. Compute the primary predictive feature
matches['Elo_Diff'] = matches['home_elo'] - matches['away_elo']

# 9. Clean and export the final training dataset
final_training_data = matches[['date', 'home_team', 'away_team', 'home_score', 'away_score', 'home_elo', 'away_elo', 'Elo_Diff', 'Match_Outcome']]
final_training_data.to_csv('wc2026_master_training_set.csv', index=False)
print(f"Dataset compiled successfully with {len(final_training_data)} modern matches.")