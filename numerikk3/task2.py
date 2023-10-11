import numpy as np

def f(x,y):
    return y**2 * np.sin(x)

x_0 = 0
y_0 = 1.0
h = 0.5

while x_0 < 1:
    y_0 = y_0 + h * f(x_0,y_0) # Tenk på y_0 som y_n her. Hva er formelen for y_n?
    x_0 = x_0 + h # Tenk på x_0 som x_n her. Hva er formelen for x_n?

svar = round(y_0, 2)
