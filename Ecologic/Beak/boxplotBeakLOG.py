import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('AVONETplusClim.csv' )

df['log_Beak_Depth'] = np.log(df['Beak.Depth'])
df = df[['Trophic.Level', 'log_Beak_Depth']].copy()
df = df[df['Trophic.Level'].isin(['Carnivore', 'Herbivore', 'Omnivore', 'Scavenger'])]
df['Trophic.Level'] = df['Trophic.Level'].astype(str)
order = ['Herbivore', 'Omnivore', 'Carnivore', 'Scavenger'] 

plt.figure(figsize=(10, 6))
sns.boxplot(x='Trophic.Level', y='log_Beak_Depth', data=df, order=order) 
plt.title('Log(Beak Depth) by Trophic Level')
plt.xlabel('Trophic Level')
plt.ylabel('Log(Beak Depth) (ln(mm))') # <-- 4. Etiket Güncellendi
plt.xticks(rotation=45) 
plt.tight_layout()

plt.savefig("boxplotBeakLOG.png")