from math import sqrt,factorial
def lagrange(x,y,point):
    n = len(x)
    result = 0
    for i in range(n):
        chisl = 1
        znam = 1
        for j in range(n):
            if j!=i:
                chisl *= point - x[j]
                znam *=x[i]-x[j] 
        result+=y[i] *(chisl/znam)
    return result


def eitken(x,y,point):
    n = len(x)
    P = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n-1):
        P[0][i] = (y[i]*(point - x[i+1]) - y[i+1]*(point-x[i])) / (x[i]-x[i+1])
    for i in range(1,n-1):
        for j in range(n-i-1):
            P[i][j] = (P[i-1][j]*(point-x[j+i+1])-P[i-1][j+1]*(point-x[j])) / (x[j]-x[j+i+1])
    result=P[n-2][0]
    print("\nТаблица Эйткена:\n")
    for i in range(n-1):
        for j in range(n-1):
            print(f"{P[i][j]:.6g}", end="\t")
        print()
    return result
def pogreshnost(point):
    m4 = 15/16
    koef = abs((point-1)*(point-2)*(point-3)*(point-4))
    eps_usech = (m4/factorial(4))*koef
    eps_okr = 10**(-3)
    eps_real = eps_okr + eps_usech
    return eps_real

if __name__=='__main__':
    x = [1,2, 3, 4]
    y = [1, 1.4142, 1.7321, 2]
    point = 2.56
    interpol_lagrange = lagrange(x, y, point)
    print ("\nФункция y = sqrt(x)\n")
    print(f"Точное значение функции для x = {point} | y = {sqrt(point)}\n\n")
    print(f"\nИнтерполяция по формуле Лагранжа для x = {point}")
    print(f"Pn({point}) = {interpol_lagrange}")

    interpol_eitken = eitken(x,y,point)
    print(f"\nИнтерполяция по формуле Эйткена для x = {point}")
    print(f"Pn({point}) = {interpol_eitken}")
    print(f"\nСравнение в точке x = {point}\n")
    print(f"Лагранж: {interpol_lagrange} (Разница: {abs(interpol_lagrange)-sqrt(point)})")
    print(f"Эйткен: {interpol_eitken} (Разница: {abs(interpol_eitken)-sqrt(point)})")

    print(f"\nРеальная погрешность = {pogreshnost(point)}")
