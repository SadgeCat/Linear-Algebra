import math, copy

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# example adjacency matrix
M = [
    [0,1,1,0,1],
    [1,0,1,1,0],
    [1,1,0,0,0],
    [0,1,0,0,1],
    [1,0,0,1,0],
]
current_matrix = M
created_matrices = []

def get_matrix(idx):
    return created_matrices[idx-1]

def set_matrix(m):
    global current_matrix
    current_matrix = m

def print_matrix():
    return matrix_to_string(current_matrix)

# converts a 2d array of edges into an adj matrix
def convert_to_adj(m, size):
    matrix = [[0] * size for _ in range(size)]
    for row in m:
        matrix[row[0]-1][row[1]-1] = 1
        matrix[row[1]-1][row[0]-1] = 1
    return matrix

# asking user for inputs to easily create a matrix
def create_matrix():
    matrix = []
    nodes = int(input("Enter the number of vertices: "))
    print("Enter (QUIT) to stop adding edges.")
    while True:
        userinput = input(f"Enter 2 numbers <= {nodes} separated by a space to make an edge between those two vertices: ")
        if userinput.lower() == 'quit':
            break
        edge = list(map(int, userinput.split()))        # converts input "a b" to [a,b] using split(), it splits by space with no parameters
        if len(edge) != 2:
            print("make sure input is valid!")
            continue
        else:
            if(edge[0] > nodes or edge[1] > nodes or edge[0] < 1 or edge[1] < 1):
                print("make sure input is valid!")
                continue
        matrix.append(edge)
    created_matrix = convert_to_adj(matrix, nodes)
    created_matrices.append(created_matrix)
    set_matrix(created_matrix)
    print(f"You created matrix #{len(created_matrices)}, access it using 'get_matrix({len(created_matrices)})'")
    print("This matrix you just created is set as your current matrix now! Set it to another matrix using 'set_matrix(*your matrix here)'")

# builds the graph using networkx and display it using matplot
def build_graph():
    for i in range(len(current_matrix)):
        for j in range(len(current_matrix[0])):
            if current_matrix[i][j] == 1:
                G.add_edge(i+1,j+1)
    nx.draw(G, with_labels=True, node_color="lightblue")
    plt.savefig('mygraph.png')
    plt.close()
    print("graphed saved!")

# Returns the dimensions of matrix A as a tuple (number of rows, number of columns)
def matrix_dimensions(A):
    num_rows = len(A)
    num_cols = len(A[0])
    return((num_rows,num_cols))

# Returns the entry in row i, column j of the matrix product A*B
def matrix_product_entry(A,B,i,j):
    t2 = matrix_dimensions(B)
    ans = 0
    for idx in range(t2[0]):
        ans += A[i][idx] * B[idx][j]
    return ans

# Returns the matrix product, time complexity is n^3
def matrix_product(A,B):
    P = []
    t1 = matrix_dimensions(A)
    t2 = matrix_dimensions(B)
    for i in range(t1[0]):
        row = []
        for j in range(t2[1]):
            row.append(matrix_product_entry(A,B,i,j))
        P.append(row)
    return P

# counts the number of paths from node i to j in k steps
# done by multiplying the adj matrix by itself, time complexity: n^3logk
def walk_count(k):
    A = copy.deepcopy(current_matrix)
    calc = [copy.deepcopy(A)]
    cnt = math.floor(math.log(k,2))             # instead of doing A*A*A*A*A*A k times, we can do this efficiently by taking A*A, then doing (A*A)(A*A), and so on
    k -= pow(2,cnt)
    for i in range(cnt):
        A = matrix_product(A,A)
        calc.append(copy.deepcopy(A))
    while k > 0:
        cnt = math.floor(math.log(k,2))         # we are essentially expressing k as a sum of powers of 2's
        k -= pow(2,cnt)
        A = matrix_product(A, calc[cnt])
    return matrix_to_string(A)

def matrix_to_string(m):
    return '\n'.join([', '.join(map(str, row)) for row in m])        # we convert ints to strs so we can join each entry of a row with , and each row with \n

print("****************************************************************")
print("This is a program that can return an adjacency matrix by calling the function 'walk_count(k)' where the entry (i,j) represents the number of walks of k steps (length k) from vertex i to j.")
print("Currently, there a built-in matrix you can play around with. See it using 'print_matrix()'")
print("You can also create a new matrix using 'create_matrix()'")
print("Create a visualization of your graph using 'build_graph()'")
print("****************************************************************")

while True:
    print(eval(input()))