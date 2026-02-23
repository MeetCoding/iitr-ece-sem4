import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE

# Load the MNIST digits dataset (64-dimensional data)
digits = load_digits()
X = digits.data  # Feature matrix (high-dimensional: 64 features)
y = digits.target  # Labels (0-9 digits)

# Visualize some input images with labels
def plot_input_images(images, labels, num_images=36):
    plt.figure(figsize=(8, 8))
    for i in range(num_images):
        plt.subplot(6, 6, i + 1)
        plt.imshow(images[i].reshape(8, 8), cmap='gray')
        plt.title(f"Label: {labels[i]}")
        plt.axis('off')
    plt.tight_layout()
    plt.show()

# Plot a few sample images
plot_input_images(digits.images, y)

# Apply t-SNE to reduce dimensionality to 2 dimensions
tsne = TSNE(n_components=2, random_state=42, perplexity=30, max_iter=1000)
X_reduced = tsne.fit_transform(X)

# Plot the t-SNE reduced data
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='tab10', s=15)
plt.colorbar(scatter, label='Digit Label')
plt.title("t-SNE Visualization of MNIST Digits")
plt.xlabel("t-SNE Dimension 1")
plt.ylabel("t-SNE Dimension 2")
plt.show()