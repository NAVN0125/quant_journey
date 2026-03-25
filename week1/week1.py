import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Broadcasting is the "magic" of NumPy (and PyTorch/TensorFlow later). It allows you to perform element-wise operations on arrays of different shapes without manually stretching the smaller array to match the larger one. This is exactly how a Neural Network adds a **Bias** vector to a **Weight** matrix.

# Here are your specific SMART tasks for mastering Broadcasting in Week 1.

# ---

# ### **Task 1: The "Manual vs. Vector" Efficiency Test**

# * **Objective:** Create a $10,000 \times 3$ matrix (representing 10,000 RGB pixels) and a $1 \times 3$ vector (representing a color shift).
# * **The Constraint:** Do not use a `for` loop to add the shift to every row.
# * **Action:** Use NumPy broadcasting to add the vector to the matrix in one line.
# * **Measurement:** Use `timeit` to compare the speed of the broadcasted operation versus a manual Python loop. (Broadcasting should be ~50-100x faster).

# pixels = np.random.randint(0, 256, (10000, 3))
# color_shift = np.array([10, 20, 30])
# pixels += color_shift
# image = Image.open("./images/image.jpg")
# image = np.array(image)
# color_shift = np.array([0, 0, 30], dtype=np.uint8)
# image = image.astype(np.uint8)
# image += color_shift
# plt.imshow(image)
# plt.show()

# ---

# ### **Task 2: Normalizing Financial Data (Z-Score)**

# In Quant, we often "center" data so the mean is 0 and the standard deviation is 1. This requires broadcasting.

# * **Objective:** Create a $100 \times 5$ array of random "stock prices" (100 days for 5 different stocks).
# * **The Math:** For each stock, subtract its specific mean and divide by its specific standard deviation.
# * **The Trick:** 1. Calculate the mean for each column (`axis=0`). This results in a $(5,)$ shape.
# 2. Use broadcasting to subtract that $(5,)$ shape from the $(100, 5)$ shape.
# * **Goal:** Prove the resulting array has a mean of 0 for every column.

# Standardization//Normalization
# stock_prices = np.random.rand(100, 5) * 100
# print(stock_prices.mean(axis=0))
# stock_prices = (stock_prices - stock_prices.mean(axis=0)) / stock_prices.std(axis=0)
# print(stock_prices.mean(axis=0))

# ---

# ### **Task 3: The "Grid Search" (Outer Product)**

# * **Objective:** Create two 1D arrays: `prices = [10, 20, 30]` and `volumes = [1, 2, 3, 4]`.
# * **The Goal:** Generate a $3 \times 4$ "Total Value" matrix where every possible price is multiplied by every possible volume.
# * **The Constraint:** You must reshape one array using `.reshape(-1, 1)` to trigger the "Outer Product" broadcast logic.
# * **SMART Result:** You should end up with a matrix where `result[0,0] = 10` and `result[2,3] = 120`.

# prices = np.array([10, 20, 30])
# volumes = np.array([1, 2, 3, 4])
# total_value = prices.reshape(-1, 1) * volumes
# print(total_value)

# ---

# ### **Task 4: Building a "Mini-Neural" Layer**

# This mimics exactly how a Deep Learning layer works.

# * **Setup:**
# * `Input_Data`: A $(64, 512)$ matrix (representing a "Batch" of 64 images/sentences, each with 512 features).
# * `Weights`: A $(512, 10)$ matrix (transforming those 512 features into 10 categories).
# * `Bias`: A $(10,)$ vector.


# * **Objective:** 1. Perform a Matrix Multiplication (`np.dot` or `@`) between `Input_Data` and `Weights`.
# 2. **Broadcast** the `Bias` vector across the resulting $(64, 10)$ matrix.
# * **Validation:** Ensure the Bias was added to every single one of the 64 rows correctly.

input_data = np.random.rand(5, 512)
weights = np.random.rand(512, 10)
bias = np.random.rand(10)
output = np.dot(input_data, weights) + bias
print(output)

# ---

# ### **The "Golden Rule" of Broadcasting**

# To succeed in these tasks, remember the **NumPy Compatibility Rule**:

# > Two dimensions are compatible when:
# > 1. They are **equal**, or
# > 2. One of them is **1**.
# > 
# > 

# **Would you like me to provide a "Starter Script" with the code to generate these random matrices so you can focus strictly on the broadcasting logic?**