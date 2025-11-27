import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('AVONETplusClim.csv' )

df['log_Mass'] = np.log(df['Mass'])
df = df[['Trophic.Level', 'log_Mass']].copy()
df = df[df['Trophic.Level'].isin(['Carnivore', 'Herbivore', 'Omnivore'])]
df['Trophic.Level'] = df['Trophic.Level'].astype(str)
order = ['Herbivore', 'Omnivore', 'Carnivore'] 

plt.figure(figsize=(10, 6))
sns.boxplot(x='Trophic.Level', y='log_Mass', data=df, order=order) 
plt.title('Log(Mass) by Trophic Level')
plt.xlabel('Trophic Level')
plt.ylabel('Log(Mass) (ln(g))')
plt.xticks(rotation=45) 
plt.tight_layout()

plt.savefig("boxplotMassTLOG.png")