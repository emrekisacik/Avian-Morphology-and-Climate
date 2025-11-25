import pandas as pd
from scipy import stats

# AVERAGE TEMP vs MASS

df = pd.read_csv('AVONETplusClim.csv' )

correlation_r, p_value = stats.pearsonr(df['bio_1'], df['Mass'])

print("--- Average Temperature and Mass ---")
print(f"Pearson r: {correlation_r:.4f}")
print(f"P-value: {p_value:.4e}")

# MINIMUM TEMP vs MASS

correlation_r, p_value = stats.pearsonr(df['bio_6'], df['Mass'])

print("--- Minimum Temperature and Mass ---")
print(f"Pearson r: {correlation_r:.4f}")
print(f"P-value: {p_value:.4e}")

# AVERAGE TEMP vs WING LENGTH

correlation_r, p_value = stats.pearsonr(df['bio_1'], df['Wing.Length'])

print("--- Average Temperature and Wing Length ---")
print(f"Pearson r: {correlation_r:.4f}")
print(f"P-value: {p_value:.4e}")

# MINIMUM TEMP vs WING LENGTH

correlation_r, p_value = stats.pearsonr(df['bio_6'], df['Wing.Length'])

print("--- Minimum Temperature and Wing Length ---")
print(f"Pearson r: {correlation_r:.4f}")
print(f"P-value: {p_value:.4e}")