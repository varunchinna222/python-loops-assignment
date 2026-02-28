#Task 2: Array Shape and Statistics

import numpy as np

scores_array = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("Shape: ", np.shape(scores_array))
print("Total elements: ", scores_array.size)
print("Highest score: ", np.max(scores_array))
print("Lowest score: ", np.min(scores_array))
print("Range: ", np.max(scores_array)-np.min(scores_array))