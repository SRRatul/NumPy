
import numpy as np
person_height = [5.2, 4, 7, 8]
person_weight = [7, 8 , 9, 6]
#array declaration
person_height = np.array(person_height)
person_weight = np.array(person_weight)
#array slicing. index wise calling.
print(person_height[2])
print(person_weight[0])
#2D array declaration
my_array = np.array([[1, 2, 3],
                     [1, 2, 3],
                     [1, 5, 3]])
print(my_array[2][1] + person_height[1])
#will print all the element of row 3
print(my_array[2])
#will print all the element of column 2
print(my_array[:,1])
my_new_array = np.array([4,8,9,10,4,5])
print(my_new_array[1:3])
my_array2= np.arange(6)
my_array3= my_new_array + my_array2
#multiply each element in the array by 2
print(my_array3*2)
# get square of each element of array
print(my_array3 ** 2)
#using Numpy with Comparison expressions
'''Check which elements are greater than or equal to 7
the comparison condition gives boolean output'''
boolean_array = my_new_array >=7
print(boolean_array)
'''We can write it like: elements of my_new_array greater than
or equal to 7'''
selected = my_new_array[boolean_array]
print(selected) #that will print the elements which are equal or greater than 7



