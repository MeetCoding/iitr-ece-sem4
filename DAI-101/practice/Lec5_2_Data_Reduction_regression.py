import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Generate Synthetic Data
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 data points (independent variable)
y = 2.5 * X + 5 + np.random.randn(100, 1)  # Linear relationship with some noise

# Visualize the original data
plt.scatter(X, y, color="blue", alpha=0.6, label="Original Data")
plt.title("Original Data")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

# Step 2: Fit a Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Predicted values
y_pred = model.predict(X)

# Step 3: Numerosity Reduction
# Represent the data using the regression line
reduced_data = np.hstack((X, y_pred))

# Step 4: Visualize the Reduction
plt.scatter(X, y, color="blue", alpha=0.3, label="Original Data")
plt.plot(X, y_pred, color="red", linewidth=2, label="Regression Line")
plt.title("Numerosity Reduction Using Linear Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# Step 5: Model Evaluation
mse = mean_squared_error(y, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Output the reduced data
print("Reduced Data (X and Predicted y):")
print(reduced_data[:10])  # Display the first 10 reduced data points