import pandas as pd
import numpy as np

df = pd.read_csv("AVONETplusClim.csv")

conditions = [
    # Aquatic/Marine
    df["Habitat"].isin(['Coastal', 'Marine', 'Riverine', 'Wetland']),
    
    # Closed/Forest
    df["Habitat"].isin(['Forest', 'Woodland', 'Shrubland']),
    
    # Open/Terrestrial
    df["Habitat"].isin(['Grassland', 'Desert', 'Rock', 'Human Modified'])
]

choices = ['Aquatic', 'Closed', 'Open']

df["Habitat"] = np.select(conditions, choices, default=None)

df.to_csv("AVONET.csv", index=False)