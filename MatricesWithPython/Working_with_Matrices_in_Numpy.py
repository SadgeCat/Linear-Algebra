# Working with Matices, Patrick Honner, 4/3/2022

# Import Numpy, Python's scientific computing library
import numpy as np

# Create a few random matrices

A = np.random.randint(-10,11,size=(3,3))
B = np.random.randint(-10,11,size=(3,5))
C = np.random.randint(-10,11,size=(2,3))


# Hardcode a few matrices
D = np.asarray([ [ 1, -2, 10], [ 0,0, 1], [3,1,-4]])
V = np.array ([-1, 5, 4])

# Built-in matrices
I_3 = np.eye(3)
Z_3 = np.zeros(3)

# Add matrices easily!
print("A = \n", A , "\n")
print ("A + I =\n", A + I_3,"\n")

# Multiply matrices with np.matmul
print ("A * B = \n", np.matmul(A,B), "\n")

# Multiply matrices with @
print ("C * B = \n", C@B, "\n")

# Raise a matrix to a power
print ("A^10 = \n",np.linalg.matrix_power(A,10), "\n")

# Compute the determinant of a matrix
print ("det(A) = \n", np.linalg.det(A), "\n")

# Solve a system 
print ("The solution to Ax= v is \n", np.linalg.solve(A,V), "\n")

# Compute the inverse of a matrix
print("The inverse of A is \n", np.linalg.inv(A), "\n")

# Find the eigenvalues and eigenvectors of a matrix

print("The eigenvalues and eigenvectors of A:\n")
for item in np.linalg.eig(A):
  print(item)

print("\n")

# Find the QR factorization of a matrix!
print ("The QR factorization of B is \n:")
for item in np.linalg.qr(B):
  print(item)