import numpy as np
import matplotlib.pyplot as plt
import pywt
import pywt.data

# Load a sample image (grayscale)
image = pywt.data.camera()

# Perform 2D Discrete Wavelet Transform (DWT)
coeffs2 = pywt.dwt2(image, 'haar')  # Using 'haar' wavelet
cA, (cH, cV, cD) = coeffs2  # Approximation, Horizontal, Vertical, Diagonal details

# Calculate data sizes
original_data_size = image.size  # Total number of pixels in the original image
approximation_data_size = cA.size  # Total number of pixels in the approximation coefficients
reduction_percentage = (1 - (approximation_data_size / original_data_size)) * 100

# Data Reduction: Retain only the approximation coefficients (cA)
# Reconstruct the image from approximation coefficients
reconstructed_image = pywt.idwt2((cA, (None, None, None)), 'haar')

# Plot the Original and Reconstructed Images
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Wavelet Decomposition
plt.subplot(1, 3, 2)
plt.imshow(cA, cmap='gray')
plt.title("Approximation Coefficients")
plt.axis('off')

# Reconstructed Image
plt.subplot(1, 3, 3)
plt.imshow(reconstructed_image, cmap='gray')
plt.title("Reconstructed Image (Data Reduced)")
plt.axis('off')

plt.tight_layout()
plt.show()

# Print Data Reduction Info
print(f"Original Data Size: {original_data_size} pixels")
print(f"Approximation Data Size: {approximation_data_size} pixels")
print(f"Data Reduction Percentage: {reduction_percentage:.2f}%")