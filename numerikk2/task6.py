import numpy as np

def f(x):
    return np.sqrt(1 + 64*x**2)

def trap(f, x):
    summa = 0
    for i in range(len(x)-1):
        h = x[i+1] - x[i]
        # temp = (h/2)*(f(x[i]) + f(x[i+1]))
        # print(temp)
        summa += (h/2)*(f(x[i]) + f(x[i+1]))
    return summa

x = np.linspace(-0.5, 2, 3+1)
print(trap(f, x))
