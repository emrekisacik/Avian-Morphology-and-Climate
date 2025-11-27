import pandas as pd
from scipy import stats

df = pd.read_csv('AVONETplusClim.csv' )

# AVERAGE TEMP vs TARSUS LENGTH

correlation_r, p_value = stats.pearsonr(df['bio_1'], df['Tarsus.Length'])

print(f"Pearson r: {correlation_r:.4f}")
print(f"P-value: {p_value:.4e}")

# MAXIMUM TEMP vs TARSUS LENGTH

correlation_r, p_value = stats.pearsonr(df['bio_5'], df['Tarsus.Length'])

print(f"Pearson r: {correlation_r:.4f}")
print(f"P-value: {p_value:.4e}")

# AVERAGE TEMP vs TAIL LENGTH

correlation_r, p_value = stats.pearsonr(df['bio_1'], df['Tail.Length'])

print(f"Pearson r: {correlation_r:.4f}")
print(f"P-value: {p_value:.4e}")

# MAXIMUM TEMP vs TAIL LENGTH

correlation_r, p_value = stats.pearsonr(df['bio_5'], df['Tail.Length'])

print(f"Pearson r: {correlation_r:.4f}")
print(f"P-value: {p_value:.4e}")

# AVERAGE TEMP vs WING LENGTH

correlation_r, p_value = stats.pearsonr(df['bio_1'], df['Wing.Length'])

print(f"Pearson r: {correlation_r:.4f}")
print(f"P-value: {p_value:.4e}")

# MAXIMUM TEMP vs WING LENGTH

correlation_r, p_value = stats.pearsonr(df['bio_5'], df['Wing.Length'])

print(f"Pearson r: {correlation_r:.4f}")
print(f"P-value: {p_value:.4e}")
