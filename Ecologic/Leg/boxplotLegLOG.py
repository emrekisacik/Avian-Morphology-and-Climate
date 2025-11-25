import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('AVONETplusClim.csv')

df['log_Tarsus'] = np.log(df['Tarsus.Length'])
df = df[df['Trophic.Level'].isin(['Carnivore', 'Herbivore', 'Omnivore', 'Scavenger'])].copy()
df['Trophic.Level'] = df['Trophic.Level'].astype(str)
order = ['Herbivore', 'Omnivore', 'Carnivore', 'Scavenger'] 

plt.figure(figsize=(10, 6))
sns.boxplot(x='Trophic.Level', y='log_Tarsus', data=df, order=order)
plt.title('Tarsus Length by Trophic Level')
plt.xlabel('Trophic Level')
plt.ylabel('log(Tarsus Length) (ln(mm))')
plt.xticks(rotation=45) 
plt.tight_layout()

plt.savefig('boxplotLegLOG.png')