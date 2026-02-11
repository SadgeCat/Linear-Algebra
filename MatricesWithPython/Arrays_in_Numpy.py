# An introduction to using Python's NumPy package (numeric python) for array handling
# We will represent matrices as arrays in Python
# Patrick Honner, 1/8/2023

# Import NumPy, Python's scientific computing package
import numpy as np

# You can create an array object by passing it a list (or a tuple)

A = np.array([1,2,3,4,5,6])
B = np.array([1,2,3,4,5,6],dtype=float)
C = np.array([[1,2,3,4,5,6.0]])
D = np.array([[1,2,3],[4,5,6]])
E = np.array((1,2,3,4,5,6,7,8))
F = np.array([[1,2],[-3,4],[0,8],[-1,-1]])

# Take a moment to consider the slight differences in how each array is defined

print("\nArray A:\n", A)

print(A.shape)

print("\nArray A^T @ A:\n", (A.reshape((1,6)).transpose()@A.reshape(1,6)))


print("\nArray B:\n", B)
print("\nArray C:\n", C)
print("\nArray D:\n", D)
print("\nArray E:\n", E)
print("\nArray F:\n", F)

# Access entries of an array using square brackets [ , ] 
# Remember! Python uses 0-indexing!
print("\nThe element in the third row, second column of F is: ", F[2,1],"\n")

# The dimensions of an array are in its shape attribute, stored as a tuple
print("\nThe dimensions of F are: ",F.shape)
print("The number of rows in F is ",F.shape[0])
print("The number of columns in F is ",F.shape[1])

# Important Note!
print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\nNote! NumPy arrays don't interpret \"row vectors\" as matrices by default")
print("\nFor example, NumPy considers the array A ", A, " to have \"shape\"", A.shape)
print("NumPy thinks of the array A as a 1-dimensional array with 6 elements")
print("\nTo make A a \"row vector\" you need to \"reshape\" it")

# Reshape the array A into a 1 x 6 row vector
A = A.reshape(1,A.shape[0])
print("\nAfter reshaping, NumPy considers the array A ", A, " to have \"shape\"", A.shape)

print("You can avoid this confusion by passing np.array a list object rather than a list:\n")
print("Notice that, by default, NumPy interprets C = np.array([[0,1,2,3,4,5,6.0]]) to have shape ",C.shape)

print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

# Import the csv package for data importing
import csv

# Importing a matrix from a file using the csv package
# This creates a list object. Each line in the file is interpreted as a comma-separted list
with open("matrix.txt") as f:
  reader = csv.reader(f)
  d = list(reader)

# This converts the list of lists of strings into a numpy array
M = np.array(d)
print("\nThe matrix imported from matrix.txt:\n",M)

# The elements of the numpy array are still strings. This converts all the elements to type float
N = M.astype(float)
print("\nThe matrix imported from matrix.txt with float entries: \n", N)



# Initialize a 2-dimensional list by creating a list of lists of 0s
P = [[0]*4 for i in range(3)]

# Here's the initialized Python list of lists
print("\nUsing list comprehensions.\n")
print("Initialized list of lists:\n", P, "\n")

# Now changes the entries programmatically
# Notice the first FOR iterates over the list of lists, the second FOR iterates over each individual list

for i in range(len(P)):
  for j in range(len(P[i])):
    P[i][j] = i + 2*j
    
print("Updated list of lists: \n", P, "\n")

# This coverts the object P from a list to a NumPy array
P = np.array(P)
print("The matrix P:\n",P, "\n")

# Examples of slicing NumPy arrays
# Notice how all slices are returned as "rows" (that is, as 1D arrays)

print("The first row of P is:", P[0], "\n")
print("The third row of P is:", P[2], "\n")
print("The first column of P is:", P[0:3,0], "\n")
print("The third column of P is:", P[0:3,2], "\n")