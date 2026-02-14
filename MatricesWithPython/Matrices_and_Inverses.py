# Matrices and Inverses
# An introduction to working with matrix inverses in NumPy
# Patrick Honner, 1/21/2023

import numpy as np
import csv

# import a matrix M from a CSV text file
with open("M_matrix.txt") as f:
  reader = csv.reader(f)
  d = list(reader)

M = np.array(d,dtype=float)

# Get the number of rows in M
n = np.shape(M)[0]


# Invert M

# Why bother doing this?
N = np.eye(n)

try:
  N = np.linalg.inv(M)
except:
  print("Can not invert A: Matrix A is singular!")


"""
# Change the matrix M so it is singular and comment out the above try - except code and run this code instead. What happens? Why?
N = np.linalg.inv(M)
"""


print("\nMatrix M: \n", M)
print("\nMatrix N, which we hope is really M^(-1): \n", N)

# Remember @ is matrix multiplication
print("\nM * N: \n",M@N)
print("\nN * M: \n",N@M)
# Notice anything strange in the output?

# Create an n x 1 column vector
b = np.array(np.random.rand(n))
b.reshape((n,1))
# Note: This reshape isn't actually necessary, as numpy will interpret b in context as necessary, but it is important to maintain awareness of the type and structure of your data at all times

# Remember, you can also multiplpy with np.matmul
print("\nN * b:\n", np.matmul(N,b))

# Solve the system Mx = b using linalg.solve()

# Why do this?
x = np.zeros(np.shape(b))

# Why is the try-except needed here?
try:
  x = np.linalg.solve(M,b)
except:
  print("Can not solve Ax = b: Matrix A is singular!")

print("\nResult of solving Mx = b: \n", x)