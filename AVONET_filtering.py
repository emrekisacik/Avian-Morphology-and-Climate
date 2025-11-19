import pandas as pd

INPUT_FILE = 'AVONET1_BirdLife.csv'
OUTPUT_FILE = 'AVONET_selected.csv'

cols_to_keep = [
    'Species1', 'Family1', 'Order1',

    'Beak.Length_Culmen', 'Beak.Width', 'Beak.Depth',
    'Tarsus.Length', 'Wing.Length', 'Hand-Wing.Index',
    'Tail.Length', 'Mass',
    
    'Habitat', 'Trophic.Level', 'Trophic.Niche', 'Primary.Lifestyle', 'Migration',

    'Range.Size', 'Min.Latitude', 'Max.Latitude',
    'Centroid.Longitude', 'Centroid.Latitude'
    
]

try:
    df = pd.read_csv(INPUT_FILE)
    
    # Select relevant columns first
    selected_cols = [c for c in cols_to_keep if c in df.columns]
    df_clean = df[selected_cols].copy()

    # Remove rows with ANY missing values in these columns
    df_clean = df_clean.dropna()

    df_clean.to_csv(OUTPUT_FILE, index=False)

except Exception as e:
    print(f"{e}")