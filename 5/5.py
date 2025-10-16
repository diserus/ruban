def lagrange(xArr,yArr,point):
    n = len(xArr)
    result = 0
    for i in range(n):
        term = yArr[i]
        for j in range(n):
            if j!=i:
                term*=(point-xArr[j])/(xArr[i]-xArr[j]) #строим базисный полином
        result+=term
    return result
if __name__=='__main__':
    x = [1, 2, 3, 4]
    y = [1, 1.4142, 1.7321, 2]
    point = 2.56

    interpolated = lagrange(x, y, point)

    print(f"{point}: {interpolated}")