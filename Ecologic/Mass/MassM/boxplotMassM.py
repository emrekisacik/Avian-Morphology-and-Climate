import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('AVONETplusClim.csv')

df_plot = df[['Migration', 'Mass']].copy()
df_plot['Migration'] = df_plot['Migration'].astype(str)
order = ['1.0', '2.0', '3.0'] 
labels = {
    '1.0': '1 (Sedentary)', 
    '2.0': '2 (Partial)', 
    '3.0': '3 (Full Migratory)'
}

plt.figure(figsize=(10, 6))
sns.boxplot(x='Migration', y='Mass', data=df_plot, order=order)
plt.title('Mass by Migration Status')
plt.xlabel('Migration Status')
plt.ylabel('Mass (g)')
plt.xticks(ticks=range(len(order)), labels=[labels[lvl] for lvl in order], rotation=45)
plt.tight_layout()

plt.savefig('boxplotMassM.png')