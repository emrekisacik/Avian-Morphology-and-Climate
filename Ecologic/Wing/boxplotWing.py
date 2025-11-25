import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('AVONETplusClim.csv')

df_plot = df[['Migration', 'Hand-Wing.Index']].copy()
df_plot['Migration'] = df_plot['Migration'].astype(str)
order = ['1.0', '2.0', '3.0'] 
labels = {
    '1.0': '1 (Sedentary)', 
    '2.0': '2 (Partial)', 
    '3.0': '3 (Full Migratory)'
}

plt.figure(figsize=(10, 6))
sns.boxplot(x='Migration', y='Hand-Wing.Index', data=df_plot, order=order)
plt.title('Hand-Wing Index by Migration Status')
plt.xlabel('Migration Status')
plt.ylabel('Hand-Wing Index (HWI)')
plt.xticks(ticks=range(len(order)), labels=[labels[lvl] for lvl in order], rotation=45)
plt.tight_layout()

plt.savefig('boxplotWing.png')