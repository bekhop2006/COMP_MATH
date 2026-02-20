import math
import matplotlib.pyplot as plt
import numpy as np






#7) From the table, compute f`(1.7489)
# x {1.73, 1.74, 1.75, 1.76, 1.77}
# y {1.772841, 1.775204, 1.777394, 1.779439, 1.781330}
# - 0.17397
# + 0.17397
# - 0.7397
# - 0.01740


#8) Construct the difference table and evaluate f(0,6)
# x {0.1, 0.3, 0.50, 0.7, 0.9, 1.1, 1.3}
# y {0.003, 0.067, 0.148, 0.248, 0.370, 0.518, 0.697}
0.2065
0.1955
0.1755
0.2955

#9 Use lagrange interpolation to estimate log10(656)
# x {654, 658, 659, 661,}
# log10(x){2.8156, 2.8182, 2.8189, 2.8202}
# 2.81604
# 2.81861
# 2.81681
# 2.81501


#10 Which equation matches the curve
# x {0, 1, 2, 3, 4}
# y {1, 1.8, 1.3, 2.5, 6.3}
# y = 1.42x^3 - 1.07x^2 - 0.55x
# y = 1.42x - 1.07x^2 - 0.55x^3
# y = 1.55x - 1.07x^2 - 1.45x^3
# y = 1.42x + 1.07x^2 - 0.55x^3

# 12 find the root of the equation f(x) = x-cos(x)
# 0.7187
# 0.1156
# 0.2194
# 0.0651

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
