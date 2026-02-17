import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Generate Synthetic Data
np.random.seed(42)
X, y = make_blobs(n_samples=300, centers=5, cluster_std=1.0, random_state=42)

# Visualize Original Data
plt.scatter(X[:, 0], X[:, 1], c='blue', alpha=0.6, label="Original Data")
plt.title("Original Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

# Step 2: Normalize the Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Perform Clustering (K-Means)
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Step 4: Data Reduction by Sampling
# Choose 10% of points from each cluster
reduced_data = []
for cluster_label in np.unique(clusters):
    cluster_points = X[clusters == cluster_label]
    sample_size = max(1, int(0.1 * len(cluster_points)))  # 10% of points
    sampled_points = cluster_points[np.random.choice(len(cluster_points), sample_size, replace=False)]
    reduced_data.append(sampled_points)

reduced_data = np.vstack(reduced_data)  # Combine all sampled points

# Visualize Reduced Data
plt.scatter(X[:, 0], X[:, 1], c='lightgray', alpha=0.3, label="Original Data")
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c='red', s=50, label="Reduced Data (Sampled)")
plt.title("Data Reduction by Clustering and Sampling")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

# Step 5: Compare Data Reduction
print(f"Original Data Size: {X.shape[0]} points")
print(f"Reduced Data Size: {reduced_data.shape[0]} points")