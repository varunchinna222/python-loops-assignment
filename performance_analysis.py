#Task 3: Performance Comparison

import numpy as np
import time

numpy_array = np.arange(1, 50001)
list_array = list(range(1, 50001))

#Numpy array sum
start_numpy = time.time()
numpy_array_sum = np.sum(numpy_array)
numpy_time = time.time() - start_numpy

# List sum
start = time.time()
list_array_sum = sum(list_array)
list_time = time.time() - start

print("NumPy sum: ", numpy_array_sum)
print("Python sum: ", list_array_sum)
print(f"NumPy time: {numpy_time:.4f} seconds")
print(f"Python time: {list_time:.4f} seconds")
print(f"NumPy is {(list_time/numpy_time):.1f}x faster")