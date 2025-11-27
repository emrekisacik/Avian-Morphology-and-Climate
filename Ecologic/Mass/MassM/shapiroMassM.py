import pandas as pd
from scipy import stats

MIGRATION_LEVELS = [1.0, 2.0, 3.0]

df = pd.read_csv('AVONETplusClim.csv')

df = df[['Migration', 'Mass']].copy()

df['Migration'] = df['Migration'].astype(float)
df = df[df['Migration'].isin(MIGRATION_LEVELS)]

for group_level in sorted(MIGRATION_LEVELS):
    group_data = df[df['Migration'] == group_level]['Mass']

    shapiro_w, shapiro_p = stats.shapiro(group_data)

    print(f"[Group {int(group_level)}] N={len(group_data)} | P-value: {shapiro_p:.4e}")