import pandas as pd
from scipy import stats

MIGRATION_LEVELS = [1.0, 2.0, 3.0]

df = pd.read_csv('AVONETplusClim.csv')

df['Migration'] = df['Migration'].astype(float)
df = df[df['Migration'].isin(MIGRATION_LEVELS)]

data_groups = [df[df['Migration'] == level]['Hand-Wing.Index'] for level in MIGRATION_LEVELS]

h_stat, p_val = stats.kruskal(*data_groups)

print(f"Groups tested: {MIGRATION_LEVELS} (1=Sedentary, 2=Partial, 3=Full)")
print(f"H-statistic: {h_stat:.4f}")
print(f"P-value: {p_val:.4e}")