import pandas as pd
from scipy import stats

SELECTED_LEVELS = ['Carnivore', 'Herbivore', 'Omnivore', 'Scavenger']

df = pd.read_csv('AVONETplusClim.csv')

df_test = df[['Trophic.Level', 'Tarsus.Length']].copy()

df_test = df_test[df_test['Trophic.Level'].isin(SELECTED_LEVELS)]

for group_name in sorted(SELECTED_LEVELS):
    group_data = df_test[df_test['Trophic.Level'] == group_name]['Tarsus.Length']
    
    shapiro_w, shapiro_p = stats.shapiro(group_data)

    print(f"[{group_name}] N={len(group_data)} | P-value: {shapiro_p:.4e}")