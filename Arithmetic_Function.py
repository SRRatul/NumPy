import numpy as np
#here is a given array
myarray = np.array([10, 20, 30, 40, 50])
'''Task: I have to calculate the sum of all elements 
of the given array. '''
print(np.sum(myarray)) #first way
print(myarray.sum()) #second way

'''Sum():
sum() function adds all the values in the array and
gives a scaler output'''

'''Task: I have to find the maximum value of the array'''
print(np.max(myarray))
print(myarray.max())

'''max():
max() function finds the maximum value in the array. '''

'''Task: I have to find the lowest value of the array'''
print(np.min(myarray)) #first way
print(myarray.min()) #second way

'''min():
min() function finds the lowest value in the array'''

'''Task: I have to raise the numbers in the array to the
power of 2'''
print(np.power(myarray, 2)) #first way

'''power():
power function raises the numbers in the array to the
given value'''


