import numpy as np
myarray = np.arange(8)
'''Split the array into 4 sub arrays. '''
print(np.split(myarray, 4))

'''Split the 1D array at positions indicated'''
#Split occurs at 2nd and 5th indices
myarray2 = np.split(myarray, [2,5])
print(myarray2)

#vsplit() //vertical split of 2d array
myarray3 = np.arange(20.0).reshape(4,5)
print(np.vsplit(myarray3, 2))
#hsplit() //horizontal split of 2d array
myarray4 = np.arange(16).reshape(4,4)
print(np.hsplit(myarray4, 2))
