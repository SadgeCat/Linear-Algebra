# Intro to Matrix Multiplication
# A starter for exploring matrix multiplication

# Import the csv module for handling data
import csv, copy

# Makes presenting a table of data easier
from tabulate import tabulate

# The matrix M is encoded as a list of lists
# Recall that the nested lists serve as the rows of the matrix

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1.2, 3]

M = [ row_1, row_2, row_3]

N = copy.deepcopy(M)

# We'll import the matrix N from a file using the CSV library
# Recall: This reads in the comma separated-values as a list of lists of strings
#                                               Each line is a list

with open("matrix.txt") as f:
  reader = csv.reader(f)
  N = list(reader)

# By default lists have strings as entries, so convert them to floats
for i in range(len(N)):
  for j in range(len (N[i])):
    N[i][j]=float(N[i][j])
    

print(tabulate(M))
print("\n")
print(tabulate(N))
print("\n")

def newMatrix():
    rows = input("Enter number of rows: ")
    cols = input("Enter number of columns: ")
    N = []
    for i in range(int(rows)):
        newRow = []
        for j in range(int(cols)):
            entry = input("Enter entry ("+str(i+1)+","+str(j+1)+"): ")
            newRow.append(float(entry))
        N.append(newRow)
    return tabulate(N)


# Challenge 1
# Write a function that returns the dimensions of a matrix


# Returns the dimensions of matrix A as a tuple (number of rows, number of columns)
def matrix_dimensions(A):
  num_rows = len(A)
  num_cols = len(A[0])
  return((num_rows,num_cols))


# Challenge 2
# Write a function that determines if two matrices can be multiplied

# Returns True or False
def can_multiply_matrices(A,B):
  t1 = matrix_dimensions(A)
  t2 = matrix_dimensions(B)
  return t1[1]==t2[0]

# Challenge 3
# Write a function that determines the entry in row i, column j of the matrix product A*B 

# Returns the entry in row i, column j of the matrix product A*B

def matrix_product_entry(A,B,i,j):
  # Should probably check first to see if the matrices can be multiplied!

  if can_multiply_matrices(A,B):
    t1 = matrix_dimensions(A)
    t2 = matrix_dimensions(B)
    row = A[i]
    ans = 0
    for idx1 in range(t2[0]):
      ans += row[idx1] * B[idx1][j]
    return ans
  else:
    return "can't be multipled"



# Challenge 4
# Write a function that multiplies two matrices A and B

# Returns the matrix product

def matrix_product(A,B):
  if not can_multiply_matrices(A,B):
    return "can't be multiplied"

  # Should probably check first to see if the matrices can be multiplied!

  # Initialize a new empty list for your row lists 
  P = []
  # Use matrix_product_entry!

  t1 = matrix_dimensions(A)
  t2 = matrix_dimensions(B)

  for i in range(t1[0]):
    row = []
    for j in range(t2[1]):
      row.append(matrix_product_entry(A,B,i,j))
    P.append(row)


  return P

# Challenge 5
# Write a function that transposes a matrix
  
def matrix_transpose(A):
  
  M = []
  t = matrix_dimensions(A)
  for i in range(t[1]):
    row = []
    for j in range(t[0]):
      row.append(A[j][i])
    M.append(row)
  return M

while True:
  print(eval(input()))