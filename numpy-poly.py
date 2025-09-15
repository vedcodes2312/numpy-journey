from numpy.polynomial import Polynomial as poly
import numpy as np
import sys
import matplotlib.pyplot as plt 

p = poly([1,2,-3])
print(type(p))
print(sys.getsizeof(p))

# representation of the polynomial 1 + 2*x - 3*x**2
print(p)

# calculate root of polynomial (1 + 2*x - 3*x**2 = 0) using numpy
roots = p.roots()
print(roots)

#evaluate at some val of x
print(p(0.345))

#derivative 
print(p.deriv())
#slope value at some val of x
print(p.deriv()(0.345))

#integral
print(p.integ())
#evaluate integral at some val of x
print(p.integ()(0.345))

#integral with constant of integration
print(p.integ(3))
#evaluate integral with constant at some val of x
print(p.integ(3)(0.345))


p1 = poly([1,2.3766,-4.55666])
# p2 = poly([0.5,0.3333,0.25],domain=[-1,1],window=[-1,1])
p2 = poly([0.5,0.3333,0.25])

#addition of polynomials
print(p1 + p2)
#subtraction of polynomials
print(p1 - p2)
#multiplication of polynomials
print(p1 * p2)
#division of polynomials
# q, r = p1 / p2 
# print("Quotient:", q)
# print("Remainder:", r)

print(p1 // p2) # returns quotient only
print(p1 % p2)  # returns remainder only

#power of polynomial
print(p1 ** 3)
#scalar multiplication
print(3 * p1)
#scalar addition
print(3 + p1)
#scalar subtraction
print(poly([3]) - p1)
#scalar division
print(p1 / 3)


#plotting the graph

x =  np.linspace(-10,10.250)
y = p(x)
z = p1(x)
q = p2(x)

plt.plot(x,y,label='p(x)')
plt.plot(x,z,label='p1(x)')
plt.plot(x,q,label='p2(x)')
plt.legend()
plt.title('Polynomial Graphs')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.show()
# A simple example to demonstrate the use of numpy's Polynomial class
# It includes polynomial creation, evaluation, differentiation, integration, arithmetic operations, and plotting.
