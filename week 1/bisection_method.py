import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 - x**2 - 2*x

def bisection(a, b, n=20):
    res = []
    for _ in range(n):
        mid = (a + b) / 2
        res.append(mid)
        if f(a) * f(mid) < 0: b = mid
        else: a = mid
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

a, b = map(float, input("a and b: ").split())
history = bisection(a, b, 20)
root = history[-1]
plot_graph(root)
print("Root:", root)
print("Iterations:", len(history))
