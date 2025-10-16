from math import *
def matrixRead():
    with open("matrix.txt", 'r') as file:
        matrix = []
        for line in file:
            row = [float(num) for num in line.strip().split()]
            matrix.append(row)
    return matrix

def matrixPrint(matrix):
    for row in matrix:
        for col in row:
            print(col,end=" ")
        print()
    print()


def calculateIterations(normC,normB,eps):
    iterations = (log((eps * (1 - normC)) / normB) / log(normC)) + 1
    return int(iterations)

def MPI(matrix,max_iter):
    n = len(matrix)

    vectorB = [0] * n 
    matrixC = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        diag = matrix[i][i]
        vectorB[i] = matrix[i][n] / diag
        for j in range(n):
            if i != j:
                matrixC[i][j] = -matrix[i][j] / diag

    x = [0]*n
    iterations = 0

    while iterations < max_iter:
        x_new = [0]*n
        for i in range(n):
            x_new[i] = sum(matrixC[i][j] * x[j] for j in range(n)) + vectorB[i]
        x = x_new
        iterations += 1
        print(f"Итерация {iterations}:", end=" ")
        for i in range(n):
            print(f"x{i+1} = {x[i]:.4f}", end=" ")
        print()
    return x, iterations

def Zeidel(matrix,max_iter):
    n = len(matrix)

    matrixC = [[0 for _ in range(n)] for _ in range(n)]
    vectorB = [0] * n

    for i in range(n):
        diag = matrix[i][i]
        vectorB[i] = matrix[i][n] / diag
        for j in range(n):
            if i != j:
                matrixC[i][j] = -matrix[i][j] / diag

    x = [0] * n
    iterations = 0

    while iterations < max_iter:
        iterations += 1
        for i in range(n):
            s = sum(matrixC[i][j] * x[j] for j in range(n))
            x[i] = s + vectorB[i]
        
        print(f"Итерация {iterations}:", end=" ")
        for i in range(n):
            print(f"x{i+1} = {x[i]:.4f}", end=" ")
        print()

    return x, iterations
if __name__ == "__main__":
    normC = 0.5
    normB = 1.8
    eps = pow(10,-3)
    max_iter = calculateIterations(normC,normB,eps)
    matrix = matrixRead()
    print("\n\nМетод простых итераций\n")
    solution, iterations = MPI(matrix,max_iter)
    for i in range(len(solution)):
        print(f"x{i+1} = {solution[i]:.4f}",end=" ")
    print("\n\nМетод Зейделя\n")
    solution, iterations = Zeidel(matrix,max_iter)
    for i in range(len(solution)):
        print(f"x{i+1} = {solution[i]:.4f}",end=" ")
