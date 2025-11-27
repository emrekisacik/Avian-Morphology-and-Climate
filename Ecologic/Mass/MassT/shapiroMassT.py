import pandas as pd
from scipy import stats

TROPHIC_LEVELS = ['Carnivore', 'Herbivore', 'Omnivore']

df_read = pd.read_csv('AVONETplusClim.csv')

df = df_read[['Trophic.Level', 'Mass']].copy()
df = df[df['Trophic.Level'].isin(TROPHIC_LEVELS)]

for group_name in sorted(TROPHIC_LEVELS):
    group_data = df[df['Trophic.Level'] == group_name]['Mass']

    shapiro_w, shapiro_p = stats.shapiro(group_data)

    print(f"[{group_name}] N={len(group_data)} | P-value: {shapiro_p:.4e}")