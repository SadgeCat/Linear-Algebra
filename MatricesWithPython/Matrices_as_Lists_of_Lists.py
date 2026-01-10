# Matrices as Lists of Lists
# A simple introduction to handling matrices as lists of lists in Python
# Patrick Honner 9/21/22

# Need this to deepcopy lists
import copy

# Makes presenting a table of data easier
from tabulate import tabulate

# We'll hardcode the matrix as a list of lists
# The nested lists function as the rows of the matrix

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]

M = [ row_1, row_2, row_3]


print("Here is matrix M shown as a table in Python:\n")
print(tabulate(M))


# Create a new copy of the matrix
# deepcopy creates a copy of values, not a copy of references
N = copy.deepcopy(M)

# Ask user to perform an elementary row operation
# row_choice = input("Choose a row to multiply by a scalar:  ")
# scalar = input("Enter a scalar to multiply by:  ")

# Convert row_choice to the appropriate index for the list
# row = int(row_choice) - 1
# Convert the string input to a float
# scalar = float(scalar)

# Perform the elementary row operation
# for i in range(len(N[row])):
#   N[row][i]=scalar*N[row][i]

# print("Here is the new matrix:")
# print(tabulate(N))

def row(n):
    return N[n-1]
def col(n):
    s = "["
    for i in range(len(N)):
        s += str(N[i][n-1])
        if i != len(N)-1:
            s += ","
    s += "]"
    return s

def changeEntry(r,c):
    newVal = input("Enter a new value for entry ("+str(r)+","+str(c)+"): ")
    N[r-1][c-1] = float(newVal)
    return tabulate(N)

def multiplyRow(n):
    scalar = input("Enter a scalar: ")
    for i in range(len(N[n-1])):
        N[n-1][i] *= float(scalar)
    return tabulate(N)

def swapRows(r1,r2):
    temp = copy.deepcopy(N[r1-1])
    N[r1-1] = copy.deepcopy(N[r2-1])
    N[r2-1] = copy.deepcopy(temp)
    return tabulate(N)

def addRows(r1,r2):
    scalar = input("Enter a scalar: ")
    for i in range(len(N[r1-1])):
        N[r2-1][i] += scalar*N[r1-1][i]
    return tabulate(N)

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

def RREF():
    for i in range(len(N)):
        pivot = N[i][i]
        while pivot == 0:
            for k in range(i+1, len(N)):
                if N[k][i] != 0:
                    swapRows(i+1, k+1)
                    pivot = N[i][i]
                    break
    

# A function to print out a list of lists, i.e. a matrix
# tabulate is nicer, so I didn't use this, but left as an example
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            # M[i][j] is the jth entry in the ith list
            # in other words, it's exactly the ij-th entry in the matrix M
            print (A[i][j], "\t", end="")
        print("\n")

while True:
    print(eval(input()))