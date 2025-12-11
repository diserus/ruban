def f(x):
    return x**2-6*x
def golden(a,b,eps):
    it = 0
    while (b-a)/2>=eps:
        it+=1
        print(f"Текущая итерация: {it}")
        lambda1=a+0.382*(b-a)
        lambda2= a+0.618*(b-a)
        if f(lambda1)>f(lambda2):
            a=lambda1
        else:
            b=lambda2
        print(f"Текущий интервал [{a} ; {b}]")
    
    x = (a+b)/2
    print(f"\n\nМинимум функции находится в интервале [ {a} ; {b}]")
    print(f"\nПриблизительное значение минимума: x = {x}")
    print(f"\nЗначение функции f({x}) = {f(x)}")
    
if __name__=="__main__":
    a=0
    b=5
    eps = 10**(-5)
    golden(a,b,eps)