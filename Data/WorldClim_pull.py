import pandas as pd
import rasterio
import os
import numpy as np

INPUT_FILE = 'AVONET_selected.csv'
OUTPUT_FILE = 'AVONETplusClim.csv'
WORLDCLIM_DIR = 'wc2.1_10m_bio' 
SELECTED_BIOS = [1, 4, 5, 6, 12]

try:
    df = pd.read_csv(INPUT_FILE)
    coords = [(x, y) for x, y in zip(df['Centroid.Longitude'], df['Centroid.Latitude'])]

    for i in SELECTED_BIOS:
        tif_path = os.path.join(WORLDCLIM_DIR, f"wc2.1_10m_bio_{i}.tif")
        if os.path.exists(tif_path):
            with rasterio.open(tif_path) as src:
                vals = []
                for x in src.sample(coords, masked=True):
                    val = x[0]
                    if np.ma.is_masked(val):
                        vals.append(np.nan)
                    else:
                        vals.append(val)
                
                df[f'bio_{i}'] = vals

    df.dropna(inplace=True)

    df.to_csv(OUTPUT_FILE, index=False)

except Exception as e:
    print(f"{e}")