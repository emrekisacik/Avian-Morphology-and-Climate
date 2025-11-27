import pandas as pd
import scikit_posthocs as sp 
import numpy as np

MIGRATION_LEVELS = [1.0, 2.0, 3.0] 

df = pd.read_csv('AVONETplusClim.csv')

df = df[['Migration', 'Mass']].copy()
df['Migration'] = df['Migration'].astype(float)
df = df[df['Migration'].isin(MIGRATION_LEVELS)]

dunn_results = sp.posthoc_dunn(a=df, 
                                val_col='Mass', 
                                group_col='Migration', 
                                p_adjust='bonferroni')

dunn_results.columns = MIGRATION_LEVELS
dunn_results.index = MIGRATION_LEVELS

print("(1=Sedentary, 2=Partial, 3=Migratory)")
print(dunn_results)