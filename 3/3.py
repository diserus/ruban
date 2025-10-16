def f(x):
    return x*x-2
def df(x):
    return 2*x
def MPD(a,b,eps):
#Делим отрезок [a,b][a,b] пополам.
#Если корень в левой части — сужаем до [a,c][a,c].
#Если в правой — до [c,b][c,b].
#Повторяем, пока длина отрезка не станет меньше eps.
    if f(a)*f(b)>=0:
        raise ValueError("Нет корня уравнения") 
    while abs(b-a)>eps:
        c = (a+b)/2
        if f(c)==0:
            break
        elif f(a)*f(c)<0:
            b = c
        elif f(c)*f(b)<0:
            a = c
    return (a+b)/2

def hord(a,b,eps):
#Строит хорду (прямая через точки (a,f(a))(a,f(a)) и (b,f(b))(b,f(b))).
#Ищет пересечение с осью xx: это новое приближение.
#Быстрее, чем бисекция, но не всегда стабилен.
    if f(a)*f(b)>=0:
        raise ValueError("Нет корня уравнения")
    c_old = a
    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))  
        if abs(c - c_old) <= eps:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c_old = c 
    return c
#Строит касательную к графику f(x)f(x), находит её пересечение с осью xx.
#Быстро сходится, если старт близко к корню.
def newton(x,eps):
    while (abs(f(x)>=eps)):
        x = x - f(x) / df(x)
    return x
if __name__ == "__main__":
    a = 1
    b=2
    eps = 10**(-6)
    print(f"Ответ: {MPD(a,b,eps)}")
    print(f"Ответ: {hord(a,b,eps)}")
    print(f"Ответ: {newton(b,eps)}")