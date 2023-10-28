import numpy as np
'''Here I will paratice on concatenation of two arrays.'''
# 1D array concatenate
array_x = np.array([2,2,3,0,1,4])
array_y = np.array([0,7,4])
print(np.concatenate([array_x, array_y]))

# 2D array concatenate
#concatenate along first axis
my_array = np.array([[2,2,3],
                    [0,1,4],
                    [0,7,4]])
print(np.concatenate([my_array, my_array]))
#concatenate along second axis
print(np.concatenate([my_array, my_array], axis=1))