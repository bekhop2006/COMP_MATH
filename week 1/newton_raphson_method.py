import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 - x**2 - 2*x

def df(x):
    return 3*x**2 - 2*x -2

def newton_raphson(x0, n=20):
    res = []
    x = x0
    for _ in range(n):
        res.append(x)
        d = df(x)
        if abs(d) < 1e-12: 
            while len(res) < n:
                res.append(x)
            break
        x = x - f(x) / d
    return res

def plot_graph(root):
    x = np.linspace(-2, 4, 1000)
    y_f = [f(xi) for xi in x]
    
    plt.plot(x, y_f, 'b-', label='f(x)', linewidth=2)
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    plt.plot(root, 0, 'ro', markersize=10, label='Корень')
    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции f(x)')
    plt.legend()
    plt.show()

x0 = float(input("x0: "))
history = newton_raphson(x0)
root = history[-1]
plot_graph(root)
print("Root:", root)
print("Iterations:", len(history))
