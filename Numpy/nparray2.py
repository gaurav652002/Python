import numpy as np
from numpy.lib.histograms import _histogram_bin_edges_dispatcher
from numpy.lib.stride_tricks import broadcast_arrays

arr = np.array([1,2,3,4,5,6])
print(arr)

# function 2 adding 2 elements of an array 
arr2 = np.array([1,2,3,4])
print(arr2[2]+arr[3])

#function 3 accesing the elements of a 2d array
arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print('2nd element on 1st dimension is:{}'.format(arr[0,2]))

# printing a normal 2 d array
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3)
print("")

# printing a 3d array
arr4 = np.array([[[1,2,3],[4,5,6],[8,9,0]]])
print(arr4)

#accessing the elements of 3d array
print("the 5th element on the 1st row and 2nd colum is {}".format(arr4[0,1,0]))
#printing a 5d array
arr5 = np.array([[[[1,2,3,],[33,3,3],[4,4,4,4],[5,5,5,5]]]])
print("the following is a 4 d array{}".format(arr5))
binary sort??? ye k 