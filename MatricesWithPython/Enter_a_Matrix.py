# Enter a Matrix from user input
# by Patrick Honner, 10/1/2022

M = []

num_rows = int(input("Enter the number of rows your matrix: "))
num_columns = int(input("Enter the number of columns of your matrix: "))

# "Initialize" the matrix by filling it with all 0.0's
# This pads the matrix with 0.0's if enough entries are not input

for i in range(num_rows):
  temp_row = []
  for j in range(num_columns):
    temp_row.append(0.0)
  M.append(temp_row)

# Read in user input, one row at a time

for i in range(num_rows):
  input_row = input("Input row "+ str(i) + " as a list of numbers separated by a comma: ")
  # input comes as a string
  # split turns the string into a list of strings, delimited by comma 
  temp_row = input_row.split(",")
  for j in range(len(temp_row)):
    M[i][j] = float(temp_row[j])
    
# A function to print out a list of lists, i.e. a matrix
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      # M[i][j] is the jth entry in the ith list
      # in other words, it's exactly the ij-th entry in the matrix M
      print (A[i][j], "\t", end="")
    print("\n")


print_matrix(M)