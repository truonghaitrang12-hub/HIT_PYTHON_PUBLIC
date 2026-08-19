
import numpy as np

print(np.__version__)
arr = np.floor(10 * np.random.random((2, 12)))
print(arr)

splitted_arr = np.hsplit(arr, 3)
print(splitted_arr)

splitted_arr_2 = np.hsplit(arr, (3, 4))
splitted_arr_2