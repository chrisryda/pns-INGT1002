import numpy as np

# definer diff-ligningen som skal løses
def f(x,y):
    return 2 * x * y

# inputs: antall steg n, steglengde h, initialverdi x0, sluttverdi xn, initialverdi y0
def improved_euler(h, x0, xn, y0):
    n = int((xn - x0) / h)
    x = np.linspace(x0, xn+h, n+2) # array med x-verdier
    y = np.zeros(n+1) # array for å lagre y-verdier
    y[0] = y0
    
    for i in range(n):
        y_pred = y[i] + h * f(x[i], y[i])
        y[i+1] = y[i] + h * ((f(x[i], y[i]) + f(x[i+1], y_pred)) / 2)
       
    return round(y[-1], 5)

x0 = 1
xn = 1.5
y0 = 1
svar_1 = improved_euler(0.1, x0, xn, y0)
svar_2 = improved_euler(0.001, x0, xn, y0)
