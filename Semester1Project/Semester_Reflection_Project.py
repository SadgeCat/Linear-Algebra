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
C = [
    [0,3,15,-1,2],
    [3,0,5,9,-1],
    [15,5,0,-1,-1],
    [-1,9,-1,0,1],
    [2,-1,-1,1,0],
]
C2 = [
    [-1,3,15,-1,2],
    [3,-1,5,9,-1],
    [15,5,-1,-1,-1],
    [-1,9,-1,-1,1],
    [2,-1,-1,1,-1],
]
# the current matrices that the user is working with, set to the examples initially
current_matrix = M
current_cost_matrix = C
current_cost_matrix2 = C2
# saves the matrices that the user created in a list so user can go back to previously created matrices if they want
created_matrices = [M]
created_cost_matrices = [C]
created_cost_matrices2 = [C2]

# standard get, set, and print functions of the matrices
def get_matrix(idx):
    return created_matrices[idx]

def get_cost_matrix(idx):
    return created_cost_matrices[idx]

def get_cost_matrix2(idx):
    return created_cost_matrices2[idx]

def set_matrix(m):
    global current_matrix
    current_matrix = m

def set_cost_matrix(m):
    global current_cost_matrix
    current_cost_matrix = m

def set_cost_matrix2(m):
    global current_cost_matrix2
    current_cost_matrix2 = m

def print_matrix():
    return matrix_to_string(current_matrix)

def print_cost_matrix():
    return matrix_to_string(current_cost_matrix)

def print_cost_matrix2():
    return matrix_to_string(current_cost_matrix2)

# converts a 2d array of edges into an adj matrix
def convert_to_adj(m, size):
    matrix = [[0] * size for _ in range(size)]
    cost_matrix = [[-1] * size for _ in range(size)]
    cost_matrix2 = [[-1] * size for _ in range(size)]
    for row in m:                           # each row is just a starting node and an ending node to represent an edge
        matrix[row[0]-1][row[1]-1] = 1
        matrix[row[1]-1][row[0]-1] = 1
        cost_matrix[row[0]-1][row[1]-1] = row[2]
        cost_matrix[row[1]-1][row[0]-1] = row[2]
        cost_matrix2[row[0]-1][row[1]-1] = row[2]
        cost_matrix2[row[1]-1][row[0]-1] = row[2]
    for i in range(size):
        cost_matrix[i][i] = 0
    return matrix, cost_matrix, cost_matrix2

# asking user for inputs to easily create a matrix and a cost matrix that indicates the cost traversing edges
def create_matrix():
    matrix = []
    nodes = int(input("Enter the number of vertices: "))
    print("Enter (QUIT) to stop adding edges.")
    while True:
        userinput = input(f"Enter 2 numbers a, b <= {nodes} and a third number c >= 0, the cost between the edge formed by node a and node b. Enter a b c separated by a space: ")
        if userinput.lower() == 'quit':
            break
        edge = list(map(int, userinput.split()))        # converts input "a b c" to [a,b,c] using split(), it splits by space with no parameters
        if len(edge) != 3:
            print("make sure input is valid!")
            continue
        else:
            if(edge[0] > nodes or edge[1] > nodes or edge[0] < 1 or edge[1] < 1):
                print("make sure input is valid!")
                continue
        matrix.append(edge)
        
    created_matrix, created_cost_matrix, created_cost_matrix2 = convert_to_adj(matrix, nodes)
    created_matrices.append(created_matrix)
    created_cost_matrices.append(created_cost_matrices)
    created_cost_matrices2.append(created_cost_matrix2)
    set_matrix(created_matrix)
    set_cost_matrix(created_cost_matrix)
    set_cost_matrix2(created_cost_matrix2)

    print(f"You created matrix #{len(created_matrices)-1}, access it using 'get_matrix({len(created_matrices)}-1)'")
    print("This matrix you just created is set as your current matrix now! Set it to another matrix using 'set_matrix(*your matrix here)'")
    print(f"You can do the same for cost_matrix and cost_matrix2 that you created. Play around with 'cost_track(k)' and 'cost_track2(k)' and see what they do!")

# builds the graph using networkx and display it using matplot
def build_graph():
    edge_labels = {}
    for i in range(len(current_matrix)):
        for j in range(len(current_matrix[0])):
            if current_matrix[i][j] == 1:
                G.add_edge(i+1,j+1)
                if i == j:
                    edge_labels[(i+1,j+1)] = "            " + str(current_cost_matrix2[i][j])
                else:
                    edge_labels[(i+1,j+1)] = current_cost_matrix2[i][j]

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

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

# we each new entry will be the min of sum of corresponding elements of the row and column vector, instead of the dot product
# this gets us the minimum cost since it takes the minimum of costs of all possible paths
def cost_entry(A,B,i,j):
    min = math.inf
    for idx in range(len(B)):
        if A[i][idx] == -1 or B[idx][j] == -1: continue
        if A[i][idx] + B[idx][j] < min:
            min = A[i][idx] + B[idx][j]
    return min

def cost_product(A,B):
    P = []
    t1 = matrix_dimensions(A)
    t2 = matrix_dimensions(B)
    for i in range(t1[0]):
        row = []
        for j in range(t2[1]):
            row.append(cost_entry(A,B,i,j))
        P.append(row)
    return P

# each resulting entry is the minimum cost of path from node i to j in at most k steps, this is done by making the cost from one node to itself 0 so you are allowed to just not move
# a nice result that follows is that the minimum cost of any path from node i to j will be the ijth entry if you let k be the length of the square matrix
def cost_track(k):
    A = copy.deepcopy(current_cost_matrix)
    B = copy.deepcopy(A)
    while k > 1:
        B = cost_product(B,A)
        k-=1
    return matrix_to_string(B)

# this version makes it so that you can't move to the node itself if there isn't an edge to itself
# therefore, this calculates the minimum cost of paths of exactly length k
def cost_track2(k):
    A = copy.deepcopy(current_cost_matrix2)
    B = copy.deepcopy(A)
    while k > 1:
        B = cost_product(B,A)
        k-=1
    return matrix_to_string(B)

# a cost of inf means that such a path DNE
# another interesting thing is that if we let d be the first k value such that no entries returned by either cost track function is inf, d is the diameter of the graph.
# this also means that for any value k >= d, 'cost_track(k)' will return the same value
# and for 'cost_track2(k)', the difference between the entries will eventually be the same for all large k's since the optimized path is to keep going back and forth along the edge with the lowest cost.

def matrix_to_string(m):
    return '\n'.join([', '.join(map(str, row)) for row in m])        # we convert ints to strs so we can join each entry of a row with , and each row with \n

print("****************************************************************")
print("This is a program that can return an adjacency matrix by calling the function 'walk_count(k)' where the entry (i,j) represents the number of walks of k steps (length k) from vertex i to j.")
print("You can also use 'cost_track(k)' to get a matrix that represents the minimum cost from 2 nodes of at most length k, and 'cost_track(2)' to get that for exactly length k")
print("Currently, there a built-in matrices you can play around with. See it using 'print_matrix()', 'print_cost_matrix()', and 'print_cost_matrix2()'")
print("You can also create a new matrix using 'create_matrix()'")
print("Create a visualization of your graph using 'build_graph()'")
print("****************************************************************")

while True:
    print(eval(input()))