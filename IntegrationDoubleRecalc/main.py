import numpy as np
def f(x): 
    return 1/x

def trapezoid(a,b,h):
    n = int((b - a) / h)+1
    x = [a + i * h for i in range(n)]
    y = [f(i) for i in x]
    result = 0
    for i in range(n-1):
        result += h * ((y[i] + y[i+1])/2)
    return result
def simpson(a,b,h):
    n = int((b - a) / h)+1
    if (n-1)%2!=0:
        print("Для Симпсона требуется четное число отрезков")
        return
    x = [a + i * h for i in range(n)]
    y = [f(i) for i in x]
    result = 0
    for i in range(0,n-2,2):
        result+=(2*h)*((1/6)*y[i] + (2/3)*y[i+1] + (1/6)*y[i+2])
    return result


if __name__ == "__main__":
    hh =0.1
    a=1
    b=2
    eps = 10**(-8)
    h = hh
    print('-' * 10, "Формула Трапеций ", '-' * 10, '\n')
    while True:
        first = trapezoid(a,b,h)
        second = trapezoid(a, b,h/2)
        print(f"h = {h}, I(h) = {first}, I(h/2) = {second}")
        if abs(first - second) < 3 * eps:
            break
        h /= 2


    h = hh
    print('-' * 10, "Формула Симпсона ", '-' * 10, '\n')

    while True:
        first = simpson(a,b,h)
        second = simpson(a,b,h/2)
        print(f"h = {h}, I(h) = {first}, I(h/2) = {second}")
        if abs(first - second) < 15 * eps:
            break
        h /= 2
