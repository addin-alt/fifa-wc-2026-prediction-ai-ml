import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score, log_loss, mean_absolute_error
import joblib

print("Initializing The Elite Stacked Trainer...")

# 1. Load the Elite Data
df = pd.read_csv('wc2026_elite_training_matrix.csv')

# Drop any lingering NaNs that might have slipped through during the shift() process
df = df.dropna()

# 2. Define our Elite Features
features = [
    'Elo_Diff', 
    'Rest_Diff', 
    'Form_Offense_Diff', 
    'Form_Defense_Diff', 
    'Elite_Offense_Diff'
]

X = df[features]
y_outcome = df['Match_Outcome'].astype(int)
y_home_goals = df['home_score']
y_away_goals = df['away_score']

# 3. Chronological Train/Test Split (80/20)
# Remember: Never use train_test_split() randomly for sports!
df = df.sort_values('date')
split_index = int(len(df) * 0.8)

X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]
y_out_train, y_out_test = y_outcome.iloc[:split_index], y_outcome.iloc[split_index:]
y_hg_train, y_hg_test = y_home_goals.iloc[:split_index], y_home_goals.iloc[split_index:]
y_ag_train, y_ag_test = y_away_goals.iloc[:split_index], y_away_goals.iloc[split_index:]

# --- LAYER 1: The Poisson Goal Predictors (Expected Goals Engine) ---
print("\nTraining Layer 1: Expected Goals (xG) Engine...")
# objective='count:poisson' forces the tree to use Poisson distribution math
xgb_home_goals = xgb.XGBRegressor(objective='count:poisson', n_estimators=100, learning_rate=0.05, max_depth=3, random_state=42)
xgb_away_goals = xgb.XGBRegressor(objective='count:poisson', n_estimators=100, learning_rate=0.05, max_depth=3, random_state=42)

xgb_home_goals.fit(X_train, y_hg_train)
xgb_away_goals.fit(X_train, y_ag_train)

hg_preds = xgb_home_goals.predict(X_test)
ag_preds = xgb_away_goals.predict(X_test)
print(f"Home Goals Mean Absolute Error: {mean_absolute_error(y_hg_test, hg_preds):.3f}")
print(f"Away Goals Mean Absolute Error: {mean_absolute_error(y_ag_test, ag_preds):.3f}")

# --- LAYER 2: The Context Classifier ---
print("\nTraining Layer 2: Elite Context Classifier...")
xgb_classifier = xgb.XGBClassifier(
    objective='multi:softprob',
    num_class=3,
    eval_metric='mlogloss',
    learning_rate=0.05,
    max_depth=4,
    n_estimators=150,
    random_state=42
)
xgb_classifier.fit(X_train, y_out_train)

y_pred = xgb_classifier.predict(X_test)
y_proba = xgb_classifier.predict_proba(X_test)

print("\n--- Classifier Performance ---")
# If Log Loss drops below 1.00, you have built a highly profitable model.
print(f"Log Loss: {log_loss(y_out_test, y_proba):.3f}") 
print(f"Accuracy: {accuracy_score(y_out_test, y_pred):.3f}")

print("\n--- Feature Importance ---")
for name, imp in zip(features, xgb_classifier.feature_importances_):
    print(f"{name}: {imp*100:.1f}%")

# --- SAVE THE BRAINS ---
joblib.dump(xgb_home_goals, 'model_home_goals.pkl')
joblib.dump(xgb_away_goals, 'model_away_goals.pkl')
joblib.dump(xgb_classifier, 'model_classifier.pkl')
print("\nAll 3 models successfully saved to disk as .pkl files!")