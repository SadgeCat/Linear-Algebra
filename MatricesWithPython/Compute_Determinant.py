import numpy as np

A1 = np.array([1,2,4,0,5,3,0,0,7],dtype=float)
A = A1.reshape((3,3))

def cm():
    size = int(input("# of rows & cols: "))
    array = []
    for i in range(size):
        for j in range(size):
            value = int(input(f"entry for row {i+1} col {j+1}: "))
            array.append(value)
    K1 = np.array(array, dtype=float)
    K = K1.reshape((size,size))
    print(K)
    return det(K)


def get_submatrix(b, row, col):
    tmp = np.delete(b, row, 0)
    tmp = np.delete(tmp, col, 1)
    return tmp

def det(M):
    size = M.shape[0]
    if size == 1:
        return M[0,0]
    else:
        for i in range(size):
            return -1 ** (i+1) * M[0,i] * det(get_submatrix(M, 0, i))

while True:
    print(eval(input()))
    