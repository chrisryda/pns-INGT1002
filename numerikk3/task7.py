def f(x,y):
    return 2 * x * y

def euler(h):
    x_0 = 1
    y_0 = 1
    
    while x_0 < 1.5 :
        y_0 = y_0 + h * f(x_0,y_0)
        x_0 = x_0 + h
        
    return round(y_0, 5)   

svar1 = euler(0.1)
svar2 = euler(0.001)
