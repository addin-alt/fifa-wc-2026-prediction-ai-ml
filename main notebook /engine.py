import pandas as pd
import numpy as np
import joblib
from collections import defaultdict
import networkx as nx

print("="*60)
print("IGNITING THE FULL WORLD CUP MONTE CARLO SIMULATOR")
print("="*60)

# 1. Load the Brains
print("[1/3] Loading AI Models from disk...")
xgb_classifier = joblib.load('model_classifier.pkl')
xgb_home_goals = joblib.load('model_home_goals.pkl')
xgb_away_goals = joblib.load('model_away_goals.pkl')

# 2. Build Current State Dictionary
print("[2/3] Compiling current team states from Elite Matrix...")
history_df = pd.read_csv('wc2026_elite_training_matrix.csv')
history_df['date'] = pd.to_datetime(history_df['date'])

team_stats = {}
all_teams = pd.concat([history_df['home_team'], history_df['away_team']]).unique()

for team in all_teams:
    team_games = history_df[(history_df['home_team'] == team) | (history_df['away_team'] == team)].sort_values('date')
    if not team_games.empty:
        last_game = team_games.iloc[-1]
        is_home = (last_game['home_team'] == team)
        team_stats[team] = {
            'elo': last_game['home_elo'] if is_home else last_game['away_elo'],
            'form_offense': last_game['home_ema_gf'] if is_home else last_game['away_ema_gf'],
            'form_defense': last_game['home_ema_ga'] if is_home else last_game['away_ema_ga'],
            'elite_offense': last_game['home_ema_offense_rating'] if is_home else last_game['away_ema_offense_rating'],
            'last_match_date': last_game['date']
        }

# 3. Load Schedule and Figure out Groups using Graph Theory
print("[3/3] Loading 2026 Schedule & mapping group structures...")
schedule = pd.read_csv('schedule_2026.csv')
schedule['Date'] = pd.to_datetime(schedule['Date'])
group_matches = schedule[schedule['Round'].str.contains('Group', na=False, case=False)]

G = nx.Graph()
for _, match in group_matches.iterrows():
    if match['home_team'] in team_stats and match['away_team'] in team_stats:
        G.add_edge(match['home_team'], match['away_team'])
groups = list(nx.connected_components(G))


# 4. Simulation Engine Helpers
def predict_match(home, away, current_date, sim_last_played):
    home_rest = min((current_date - sim_last_played[home]).days, 30)
    away_rest = min((current_date - sim_last_played[away]).days, 30)
    
    vec = pd.DataFrame([[
        team_stats[home]['elo'] - team_stats[away]['elo'],
        home_rest - away_rest,
        team_stats[home]['form_offense'] - team_stats[away]['form_offense'],
        team_stats[home]['form_defense'] - team_stats[away]['form_defense'],
        team_stats[home]['elite_offense'] - team_stats[away]['elite_offense']
    ]], columns=['Elo_Diff', 'Rest_Diff', 'Form_Offense_Diff', 'Form_Defense_Diff', 'Elite_Offense_Diff'])
    
    probs = xgb_classifier.predict_proba(vec)[0]
    result = np.random.choice([0, 1, 2], p=probs)
    
    hg_xg = xgb_home_goals.predict(vec)[0]
    ag_xg = xgb_away_goals.predict(vec)[0]
    
    return result, hg_xg, ag_xg


# 5. The Main Loop
ITERATIONS = 1000
tournament_wins = defaultdict(int)
finalist_appearances = defaultdict(int)

print("\n" + "="*60)
print(f"STARTING {ITERATIONS} MULTIVERSE SIMULATIONS...")
print("="*60)

for i in range(ITERATIONS):
    # >>> PROGRESS TRACKER TERMINAL OUTPUT <<<
    if (i + 1) % 100 == 0:
        print(f"[*] Simulating Tournament {i + 1} of {ITERATIONS}...")

    pts = defaultdict(int)
    xg_diff = defaultdict(float)
    sim_last_played = {t: s['last_match_date'] for t, s in team_stats.items()}
    
    # --- PHASE 1: GROUP STAGE ---
    for _, match in group_matches.iterrows():
        home, away, date = match['home_team'], match['away_team'], match['Date']
        if home not in team_stats or away not in team_stats: continue
            
        result, hg_xg, ag_xg = predict_match(home, away, date, sim_last_played)
        
        xg_diff[home] += (hg_xg - ag_xg)
        xg_diff[away] += (ag_xg - hg_xg)
        
        if result == 2: pts[home] += 3
        elif result == 0: pts[away] += 3
        else: pts[home] += 1; pts[away] += 1
            
        sim_last_played[home] = date
        sim_last_played[away] = date

    advancing_32 = []
    third_places = []
    
    for group in groups:
        group_teams = list(group)
        group_teams.sort(key=lambda x: (pts[x], xg_diff[x]), reverse=True)
        if len(group_teams) >= 2:
            advancing_32.extend(group_teams[:2]) 
        if len(group_teams) >= 3:
            third_places.append(group_teams[2]) 
            
    third_places.sort(key=lambda x: (pts[x], xg_diff[x]), reverse=True)
    advancing_32.extend(third_places[:8])
    advancing_32.sort(key=lambda x: (pts[x], xg_diff[x]), reverse=True)
    
    # --- PHASE 2: KNOCKOUT BRACKET ---
    current_round = advancing_32
    ko_date = date + pd.Timedelta(days=5) 
    
    while len(current_round) > 1:
        next_round = []
        for match_idx in range(len(current_round) // 2):
            team_a = current_round[match_idx]
            team_b = current_round[len(current_round) - 1 - match_idx]
            
            result, a_xg, b_xg = predict_match(team_a, team_b, ko_date, sim_last_played)
            
            if result == 1: 
                winner = team_a if a_xg > b_xg else team_b
            elif result == 2:
                winner = team_a
            else:
                winner = team_b
                
            next_round.append(winner)
            sim_last_played[team_a] = ko_date
            sim_last_played[team_b] = ko_date
            
        if len(next_round) == 2:
            finalist_appearances[next_round[0]] += 1
            finalist_appearances[next_round[1]] += 1
            
        current_round = next_round
        ko_date += pd.Timedelta(days=4)
        
    champion = current_round[0]
    tournament_wins[champion] += 1

# 6. Final Outputs
print("\n" + "="*60)
print("🏆 --- 2026 FIFA WORLD CUP: PREDICTED CHAMPIONS --- 🏆")
print("="*60)
print(f"{'Team':<25} | {'Win Probability':<18} | {'Reach Final %'}")
print("-" * 65)

sorted_champs = sorted(tournament_wins.items(), key=lambda x: x[1], reverse=True)
for team, wins in sorted_champs[:15]:
    win_pct = (wins / ITERATIONS) * 100
    final_pct = (finalist_appearances[team] / ITERATIONS) * 100
    print(f"{team:<25} | {win_pct:>16.1f}% | {final_pct:>11.1f}%")

print("\nSimulation complete. The numbers don't lie.")