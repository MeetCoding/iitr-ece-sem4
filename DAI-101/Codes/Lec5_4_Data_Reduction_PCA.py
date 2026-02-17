# EXAMPLE FOR DATA CLEANING OUTLIER REMOVAL
# DR. DEVESH BHIMSARIA

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load dataset (Iris dataset)
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.DataFrame(data.target, columns=["Target"])

# Display original dataset shape
print("Original Dataset Shape:", X.shape)

# Standardize the data (mean=0, variance=1) - Needed for PCA
scaler = StandardScaler() # 	This creates an instance of the StandardScaler class
X_scaled = scaler.fit_transform(X)

# Apply PCA (reduce to 2 dimensions for visualization)
pca = PCA(n_components=2)  # Specify number of components
X_pca = pca.fit_transform(X_scaled)

# Display the reduced dataset shape
print("Reduced Dataset Shape:", X_pca.shape)

# Explained variance ratio (how much variance is retained)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
# The explained variance ratio tells you how much of the total variance in the original data is captured by each principal component (PC).

print("Total Variance Retained:", sum(pca.explained_variance_ratio_))

# Convert to DataFrame for visualization
X_pca_df = pd.DataFrame(X_pca, columns=['Principal Component 1', 'Principal Component 2'])
X_pca_df['Target'] = y

# Visualize the reduced data
plt.figure(figsize=(8, 6))
colors = ['red', 'blue', 'green']
for i in range(3):
    subset = X_pca_df[X_pca_df['Target'] == i]
    plt.scatter(subset['Principal Component 1'], subset['Principal Component 2'],
                label=data.target_names[i], color=colors[i], alpha=0.7)
plt.title("PCA: Reduced to 2 Dimensions")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.grid()
plt.show()


# Apply PCA (reduce to 3 dimensions for visualization)
pca = PCA(n_components=3)  # Specify number of components
X_pca = pca.fit_transform(X_scaled)

# Display the reduced dataset shape
print("Reduced Dataset Shape:", X_pca.shape)

# Explained variance ratio (how much variance is retained)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
# The explained variance ratio tells you how much of the total variance in the original data is captured by each principal component (PC).

print("Total Variance Retained:", sum(pca.explained_variance_ratio_))