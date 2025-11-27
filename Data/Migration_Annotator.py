import pandas as pd

df = pd.read_csv('AVONETplusClim.csv')

migration_map = {
    1.0: 'Sedentary',
    2.0: 'Partial',
    3.0: 'Migratory'
}

df['Migration'] = df['Migration'].map(migration_map)

df.to_csv('AVONETplusClim_migration.csv', index=False)