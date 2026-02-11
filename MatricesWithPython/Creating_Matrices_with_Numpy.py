# Creating Matrices with numpy
# A variety of examples of generating matrices 
# Patrick Honner, 1/8/2023

# Import NumPy, Python's scientific computing package
import numpy as np

# Import random, Python's random number package
import random

# Creating an array by converting lists using asarray
A1 = np.array([1,2,3,4,5,6],dtype=float)

print ("Simple list converted to array A1:\n", A1)
print("\n")

# Creating multi-dimensional arrays using lists of lists
A2 = np.array ([[1,2],[3,4],[5,6]],dtype=float)

print("List of lists converted to array A2: \n",A2)
print("\n")

# You can re-shape arrays
A3 = A1.reshape((2,3))
print("The row vector A1 reshaped as a 2x3 matrix A3: \n",A3,"\n")

# Some built-in matrices

# np.zeros creates an all-zeroes array 
# dimensions are passed as a tuple (number of rows, number of columns)
B3 = np.zeros((2,3))
print("A 2x3 all-zeroes array: \n",B3)
print("\n")

# np.zeros creates an all-zeroes array 
# dimensions are passed as a tuple (number of rows, number of columns)
B3 = np.ones((5,2))
print("A 5x2 all-1s array: \n",B3)
print("\n")

# numpy has built-in identity matrix functions
I1 = np.eye(4)
I2 = np.eye(4,6)

print ("A 4x4 identity matrix: \n", I1, "\n")
print ("A 4x4 identity matrix with two additional columns of 0s: \n", I2, "\n")

# Numpy has built-in diagonal matrix functions
D1 = np.diag([-4,3,0,1])
D2 = np.diag([2,-1,3], 2 )

print ("A diagonal matrix with given entries:\n", D1, "\n")
print ("A diagonal matrix with given entries and two leading columns of 0s: \n", D2, "\n")

# The function diag can also return the diagonal entries of an existing matrix
print("The diagonal elements of the matrix \n" , A2, "\n are \n" , np.diag(A2), "\n")


# arange and linspace

# Numpy's arange creates 1D arrays of consecutive integers
C1 = np.arange(3,12,dtype=float)
print("np.arange creates a 1D sequence of consecutive integers: \n", C1, "\n")
print("Which you can reshape into a multi-dimensional array: \n", C1.reshape(3,3),"\n")

# Nummpy's linspace creates arithmetic sequences
C2 = np.linspace(4., .25,16)
print("np.linspace creates a 1D arithmetic progression: \n", C2, "\n")
print("Which can also be reshaped: \n", C2.reshape(4,4), "\n")

# Random Matrices!

# Notice np.random.random takes dimensions as a tuple

R1 = np.random.random((3,3))

print("A 3x3 matrix of random numbers uniformly drawn from 0 to 1:\n", R1, "\n")

R2 = np.random.uniform(-1,1,(3,3))

print("A random 3x3 matrix with uniform entries between -1 and 1: \n", R2, "\n")

# Randint returns random integers. NOTE the parameter is upper bound + 1
R3 = np.random.randint(2,size = (4,4))
R4 = np.random.randint(-10,10,size =(3,3))

print("A random 4x4 matrix with all entries 0 or 1:\n", R3, "\n")
print("A random 3x3 matrix with all entries between -10 and 9:\n", R4, "\n")

