#Task 1: Create an Array and Basic Math
import numpy as np

temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = temps_celsius * 1.8 + 32
print("Celsius: ",temps_celsius)
print("Fahrenheit: ",temps_fahrenheit)
print("Average Fahrenheit: ",f"{(np.sum(temps_fahrenheit)/temps_fahrenheit.size):.1f}")