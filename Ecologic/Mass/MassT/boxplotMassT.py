import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('AVONETplusClim.csv' )

df_plot = df[['Trophic.Level', 'Mass']].copy()
df_plot = df_plot[df_plot['Trophic.Level'].isin(['Carnivore', 'Herbivore', 'Omnivore'])]
df_plot['Trophic.Level'] = df_plot['Trophic.Level'].astype(str)
order = ['Herbivore', 'Omnivore', 'Carnivore'] 

plt.figure(figsize=(10, 6))
sns.boxplot(x='Trophic.Level', y='Mass', data=df_plot, order=order) 
plt.title('Mass by Trophic Level')
plt.xlabel('Trophic Level')
plt.ylabel('Mass (g)')
plt.xticks(rotation=45) 
plt.tight_layout()

plt.savefig("boxplotMassT.png")