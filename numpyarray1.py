import numpy as np

arr1 = np.array([1,2,3,4,5,])  #one dimensional array

arr2 = np.array([[1,2,3],[4,5,6]])  #two dimensional array

arr3 = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])  #three dimensional array

print("One-dimensional array:")
print(arr1)

print("Two-dimensional array:")
print(arr2)

print("Three-dimensional array:")
print(arr3)

arr4 = np.array([[[[1,2],[3,4]], [[5,6],[7,8]]], [[[9,10],[11,12]], [[13,14],[15,16]]]])  #four dimensional array

print("Four-dimensional array:")
print(arr4)

arr5 = np.array([1, 2, 3, 4, 5], ndmin=5)  #five dimensional array
print("Five-dimensional array:")
print(arr5)

print(arr1.ndim)  #prints the number of dimensions of arr1
print(arr2.ndim)  #prints the number of dimensions of arr2
print(arr3.ndim)  #prints the number of dimensions of arr3
print(arr4.ndim)  #prints the number of dimensions of arr4
print(arr5.ndim)  #prints the number of dimensions of arr5

print("Shape of arr1:", arr1.shape)  #prints the shape of arr1
print("Shape of arr2:", arr2.shape)
print("Shape of arr3:", arr3.shape)  #prints the shape of arr3
print("Shape of arr4:", arr4.shape)  #prints the shape of arr4
print("Shape of arr5:", arr5.shape)  #prints the shape of arr5

print("Size of arr1:", arr1.size)  #prints the size of arr1
print("Size of arr2:", arr2.size)  #prints the size of arr2
print("Size of arr3:", arr3.size)  #prints the size of arr3
print("Size of arr4:", arr4.size)  #prints the size of arr4
print("Size of arr5:", arr5.size)  #prints the size of arr5

print("Data type of arr1:", arr1.dtype)  #prints the data type of arr1
print("Data type of arr2:", arr2.dtype)
print("Data type of arr3:", arr3.dtype)  #prints the data type of arr3
print("Data type of arr4:", arr4.dtype)  #prints the data type of arr4
print("Data type of arr5:", arr5.dtype)  #prints the data type of arr5

print("Item size of arr1:", arr1.itemsize)  #prints the item size of arr1
print("Item size of arr2:", arr2.itemsize)
print("Item size of arr3:", arr3.itemsize)  #prints the item size of arr3
print("Item size of arr4:", arr4.itemsize)  #prints the item size of arr4
print("Item size of arr5:", arr5.itemsize)  #prints the item size of arr5

print("Memory size of arr1:", arr1.nbytes)  #prints the memory size of arr1
print("Memory size of arr2:", arr2.nbytes)  #prints the memory size of arr2
print("Memory size of arr3:", arr3.nbytes)  #prints the memory size of arr3
print("Memory size of arr4:", arr4.nbytes)  #prints the memory size of arr4
print("Memory size of arr5:", arr5.nbytes)  #prints the memory size of arr5

