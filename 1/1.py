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
            print(int(col),end=" ")
        print()
    print()
def gauss(matrix):
    n = len(matrix)
    for i in range(n):
        mainn = matrix[i][i] 
        str_main = i 
        for j in range(i,n): 
            if abs(matrix[j][i]) > abs(mainn): 
                mainn = matrix[j][i] 
                str_main = j 
        matrix[i],matrix[str_main] = matrix[str_main],matrix[i]
        for j in range(i + 1, n):
            a = matrix[j][i] / mainn
            for k in range(i, n + 1):  
                matrix[j][k] -= a * matrix[i][k]
        
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += matrix[i][j] * x[j]
        x[i] = (matrix[i][n] - s) / matrix[i][i]
    
    return x
if __name__ == "__main__":
    matrix = matrixRead()
    print("Исходная матрица")
    matrixPrint(matrix)
    print("Решение методом Гаусса")
    solution = gauss(matrix)
    for i in solution:
        print(f"x = {i}")