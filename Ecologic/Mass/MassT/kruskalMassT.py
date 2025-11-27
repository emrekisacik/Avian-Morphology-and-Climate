import pandas as pd
from scipy import stats

df = pd.read_csv('AVONETplusClim.csv')

df_test = df[['Trophic.Level', 'Mass']].copy()

df_test = df_test[df_test['Trophic.Level'].isin(['Carnivore', 'Herbivore', 'Omnivore'])]

groups = sorted(df_test['Trophic.Level'].unique())
data_groups = [df_test[df_test['Trophic.Level'] == g]['Mass'] for g in groups]

h_stat, p_val = stats.kruskal(*data_groups)

print(f"Groups tested: {groups}")
print(f"H-statistic: {h_stat:.4f}")
print(f"P-value: {p_val:.4e}")