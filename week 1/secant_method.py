import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 - x**2 - 2*x

def secant(x0, x1, n=20):
    res = []
    for _ in range(n):
        res.append(x0)
        fx0, fx1 = f(x0), f(x1)
        if abs(fx1 - fx0) < 1e-15:
            while len(res) < n:
                res.append(x1)
            break
        x_next = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x_next
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

x0, x1 = map(float, input("x0 x1: ").split())
history = secant(x0, x1)
root = history[-1]
plot_graph(root)
print("Root:", root)
print("Iterations:", len(history))
