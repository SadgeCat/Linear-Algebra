# Challenge -- Convert an Incidence Matrix to a NetworkX Graph
# 
# Write a program that converts an indcidence matrix into a NetworkX graph object, then draw the graph
# Bonus: First verify that the matrix is a legitimate incidence matrix first!
# Bonus: Write a program that converts a NetworkX graph object into an incidence matrix

# Import the NetworkX package for creating graphs, matplotlib.pyplot for plotting them
import networkx as nx
import matplotlib.pyplot as plt

# Hard-coded Incidence matrix. Play around and make changes to test your program.
M = [[1,-1,0,0,0],[1,0,-1,0,0],[1,0,0,-1,0],[0,1,-1,0,0],[0,1,0,-1,0], [0,1,0,0,-1],[0,0,1,-1,0]]

example_row_1 = [0,0,0,0,0,1,0,0,-1]
example_row_2 = [0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

# A helpful piece of code:
# The index method return the index number of a element of a list

print(example_row_1,example_row_1.index(1))
print(example_row_2,example_row_2.index(-1))

e = (example_row_1.index(1),example_row_2.index(-1))

print(e)