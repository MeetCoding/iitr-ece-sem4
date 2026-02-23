# EXAMPLE FOR DATA CLEANING OUTLIER REMOVAL
# DR. DEVESH BHIMSARIA

import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'ID': range(1, 21),
    'Age': [22, 25, 30, 24, 29, 35, 120, 28, 32, 31, 27, 26, 23, 40, 33, 29, 36, 100, 28, 29]
}
df = pd.DataFrame(data)

# Display original data
print("Original Dataset:")
print(df)

# Plot boxplot to visualize outliers
plt.figure(figsize=(8, 5))
plt.boxplot(df['Age'], vert=False, patch_artist=True, boxprops=dict(facecolor="skyblue"))
plt.title("Boxplot of Age with Outliers")
plt.xlabel("Age")
plt.show()

# Calculate IQR for outlier detection
Q1 = df['Age'].quantile(0.25)  # First quartile (25th percentile)
Q3 = df['Age'].quantile(0.75)  # Third quartile (75th percentile)
IQR = Q3 - Q1  # Interquartile range

# Define lower and upper bounds for outlier detection
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"\nLower Bound: {lower_bound}, Upper Bound: {upper_bound}")

# Identify outliers
outliers = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
print("\nOutliers Detected:")
print(outliers)

# Remove outliers
df_cleaned = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df_cleaned)

# Plot boxplot after removing outliers
plt.figure(figsize=(8, 5))
plt.boxplot(df_cleaned['Age'], vert=False, patch_artist=True, boxprops=dict(facecolor="lightgreen"))
plt.title("Boxplot of Age After Outlier Removal")
plt.xlabel("Age")
plt.show()