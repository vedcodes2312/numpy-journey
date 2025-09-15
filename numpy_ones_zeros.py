# zeros and ones 

import numpy as np

a = np.zeros(5)
b = np.zeros((2,3),dtype=int)
print("a=",a)
print("b=\n",b)

a = np.ones(5)
b = np.ones((2,3),dtype=int)
print("a=",a)
print("b=\n",b)

arr = np.array([[1,2,3,{1,2,3,4}],[4,5, 6+3j,"ved"]],dtype=object)
print(arr)
z = np.zeros_like(arr)
o = np.ones_like(arr)
print("zeros\n",z)
print("ones\n",o)

# b = np.ones((3, 4))
# c = np.full((2, 3), 7)
# d = np.eye(4)
# e = np.random.rand(2, 2)
# f = np.random.randint(1, 10, (3, 3))
# g = np.linspace(0, 1, 5)
# h = np.arange(0, 10, 2)
# i = np.empty((2, 2))