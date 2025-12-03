import numpy as np

n = 99
my_array = np.arange(0, n + 1)
my_array = np.roll(my_array, 50)


print(my_array)


# Right circular shift by 2 positions
shifted_array_right = np.roll(my_array, 2)
print(shifted_array_right)  # Output: [4 5 1 2 3]

# Left circular shift by 2 positions
shifted_array_left = np.roll(my_array, -2)
print(shifted_array_left)  # Output: [3 4 5 1 2]