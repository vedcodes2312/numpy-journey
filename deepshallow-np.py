# deep copy and shallow copy
import numpy as np

a = np.array([1.233, 2.3456, 3.45678], dtype = np.float32)

b = a # shallow copy, b is just a reference to a
c = a.copy() # deep copy, c is a new array
# deep copy is independent

d = a.view()  #another way of shallow copy 
#shallow copy - changes in original affect it
# not in deep copy

a[0] = 3.444555

print(b) # deep copy
print(c) # shallow copy
print(d)  #shallow copy  
