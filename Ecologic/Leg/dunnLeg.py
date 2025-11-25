import pandas as pd
import scikit_posthocs as sp 
import numpy as np

df = pd.read_csv('AVONETplusClim.csv')

df_test = df[['Trophic.Level', 'Tarsus.Length']].dropna().copy()
df_test = df_test[df_test['Trophic.Level'].isin(['Carnivore', 'Herbivore', 'Omnivore', 'Scavenger'])]

dunn_results = sp.posthoc_dunn(a=df_test, 
                                val_col='Tarsus.Length', 
                                group_col='Trophic.Level', 
                                p_adjust='bonferroni')

groups = sorted(df_test['Trophic.Level'].unique())
dunn_results.columns = groups
dunn_results.index = groups

print(dunn_results)
