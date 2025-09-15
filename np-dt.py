# numpy data types
import numpy as np
import sys
#integer datatype
a1 = np.array([1,2,3,4,5],dtype=np.int32)
print(a1)
print(sys.getsizeof(a1))
print(a1.dtype)
print(a1.itemsize)
print(a1.size)
print(a1.nbytes)
print(type(a1))
print(a1.shape)
print(a1.ndim)
print(a1.data)

#complex datatype
a2 = np.array([1+2j, 3+10j, 100+5j],dtype=np.complex128)
print(a2)
print(sys.getsizeof(a2))

#boolean datatype
a3 = np.array([True,False,True],dtype=np.bool_)
print(a3)
print(sys.getsizeof(a3))

# float datatype
a4 = np.array([1.2345688, 3.45533, 8.9182828], dtype=np.float32)
print(a4)
print(sys.getsizeof(a4))

# object datatype
a5 = np.array([1, "ved", {1,2,3,4,5,5}, {1:0,2:5}],dtype=np.object_)
print(a5)
print(sys.getsizeof(a5))

# void datatype - like structure union in C/C++
dt = np.dtype([('name','U10'),('age,','i4')])
a6 = np.array([("ABC",14),("XYZ",10)],dtype=dt)
print(a6)
print(sys.getsizeof(a6))



