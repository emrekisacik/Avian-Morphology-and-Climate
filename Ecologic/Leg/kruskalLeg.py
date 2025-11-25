import pandas as pd
from scipy import stats

df = pd.read_csv('AVONETplusClim.csv')

df = df[df['Trophic.Level'].isin(['Carnivore', 'Herbivore', 'Omnivore', 'Scavenger'])]

groups = sorted(df['Trophic.Level'].unique())
data_groups = [df[df['Trophic.Level'] == g]['Tarsus.Length'] for g in groups]

h_stat, p_val = stats.kruskal(*data_groups)

print(f"Groups tested: {groups}")
print(f"H-statistic: {h_stat:.4f}")
print(f"P-value: {p_val:.4e}")
