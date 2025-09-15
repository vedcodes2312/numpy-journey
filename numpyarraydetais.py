#numpy function
import numpy as np
a = np.array(43)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)
d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

#ndim - tells array dimensions-returns an integer
print(a.ndim, b.ndim, c.ndim, d.ndim)


#shape - returns a tuple of array dimensions
print(a.shape, b.shape, c.shape, d.shape)

#size - returns total number of elements in the array
print(a.size, b.size, c.size, d.size)

#dtype - returns the data type of the array elements
print(a.dtype, b.dtype, c.dtype, d.dtype)

#itemsize - returns the size in bytes of each element in the array
print(a.itemsize, b.itemsize, c.itemsize, d.itemsize)

#nbytes - returns the total size in bytes of the array
print(a.nbytes, b.nbytes, c.nbytes, d.nbytes)

#type - returns the type of the array
print(type(a), type(b), type(c), type(d))
arr = np.array([1,2,3,4,5,6], ndmin=10)
print(arr)