import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Load the Iris Dataset
iris = load_iris()
X = iris.data  # Features (4 features: sepal length, sepal width, petal length, petal width)
y = iris.target  # Labels (3 classes: Setosa, Versicolor, Virginica)
target_names = iris.target_names  # Class names

# Step 2: Standardize the Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply PCA for Dimensionality Reduction
pca = PCA(n_components=3)  # Reduce to 3 principal components
X_pca = pca.fit_transform(X_scaled)

# Print Explained Variance Ratios
explained_variance_ratios = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance_ratios)
print("Explained Variance Ratios:", explained_variance_ratios)
print("Cumulative Variance Retained:", cumulative_variance)

# Step 4: Create a 3D Scatter Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot each class in a different color
for i, target_name in enumerate(target_names):
    ax.scatter(
        X_pca[y == i, 0],  # PC1
        X_pca[y == i, 1],  # PC2
        X_pca[y == i, 2],  # PC3
        label=target_name,
        s=50
    )

# Add labels and legend
ax.set_title('3D Scatter Plot of PCA on Iris Dataset', fontsize=15)
ax.set_xlabel('Principal Component 1', fontsize=12)
ax.set_ylabel('Principal Component 2', fontsize=12)
ax.set_zlabel('Principal Component 3', fontsize=12)
ax.legend(target_names, fontsize=10)

plt.show()