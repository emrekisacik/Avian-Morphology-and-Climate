import pandas as pd
import scikit_posthocs as sp 
import numpy as np

df = pd.read_csv('AVONETplusClim.csv')

df = df[['Trophic.Level', 'Beak.Depth']].copy()
df = df[df['Trophic.Level'].isin(['Carnivore', 'Herbivore', 'Omnivore', 'Scavenger'])]

dunn_results = sp.posthoc_dunn(a=df, 
                                val_col='Beak.Depth', 
                                group_col='Trophic.Level', 
                                p_adjust='bonferroni')

groups = sorted(df['Trophic.Level'].unique())
dunn_results.columns = groups
dunn_results.index = groups

print(dunn_results)