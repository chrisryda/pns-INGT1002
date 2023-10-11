import numpy as np

def f(x,y):
    return x + np.sqrt(y)

x_0 = 0
y_0 = 0
h = 0.2

while x_0 < 1:
    y_0 = y_0 = y_0 + h * f(x_0,y_0)
    x_0 = x_0 = x_0 + h
    
svar = round(y_0, 2)
