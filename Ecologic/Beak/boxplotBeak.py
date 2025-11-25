import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('AVONETplusClim.csv' )

df_plot = df[['Trophic.Level', 'Beak.Depth']].copy()
df_plot = df_plot[df_plot['Trophic.Level'].isin(['Carnivore', 'Herbivore', 'Omnivore', 'Scavenger'])]
df_plot['Trophic.Level'] = df_plot['Trophic.Level'].astype(str)
order = ['Herbivore', 'Omnivore', 'Carnivore', 'Scavenger'] 

plt.figure(figsize=(10, 6))
sns.boxplot(x='Trophic.Level', y='Beak.Depth', data=df_plot, order=order) 
plt.title('Beak Depth by Trophic Level')
plt.xlabel('Trophic Level')
plt.ylabel('Beak Depth (mm)')
plt.xticks(rotation=45) 
plt.tight_layout()

plt.savefig("boxplotBeak.png")