import math
import matplotlib.pyplot as plt

# Функция и производная
def f(x):
    return x**3 - x**2 - 2*x

def df(x):
    return 3*x**2 - 2*x -2

def bisection(a, b, n=20):
    res = []
    for _ in range(n):
        mid = (a + b) / 2
        res.append(mid)
        if f(a) * f(mid) < 0: b = mid
        else: a = mid
    return res

def fixed_point(x0, n=7):
    res = []
    x = x0
    for _ in range(n):
        res.append(x)
        x = math.sqrt(x + 2)
    return res

def newton_raphson(x0, n=7):
    res = []
    x = x0
    for _ in range(n):
        res.append(x)
        d = df(x)
        if abs(d) < 1e-12: break
        x = x - f(x) / d
    return res

def secant(x0, x1, n=7):
    res = []
    for _ in range(n):
        res.append(x0)
        fx0, fx1 = f(x0), f(x1)
        if abs(fx1 - fx0) < 1e-15: break
        x_next = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x_next
    return res

n_iters = 20
history_bis = bisection(1.2, 3.2, n_iters)
history_fix = fixed_point(3.0, n_iters)
history_new = newton_raphson(2.0, n_iters)
history_sec = secant(3.2, 2.8, n_iters)

col = 15
header = ["Iteration", "Bisection", "Fixed-Point", "Newton", "Secant"]
print("\n" + "="*75)
print("".join(f"{h:<{col}}" for h in header))
print("-" * 75)

for i in range(n_iters):
    row = f"x{i:<{col-1}}"
    row += f"{history_bis[i]:<{col}.6f}"
    row += f"{history_fix[i]:<{col}.6f}"
    row += f"{history_new[i]:<{col}.6f}"
    row += f"{history_sec[i]:<{col}.6f}"
    print(row)
print("="*75)

plt.figure(figsize=(10, 6))
iters = range(n_iters)

plt.plot(iters, history_bis, label='Bisection', marker='o', linewidth=2)
plt.plot(iters, history_fix, label='Fixed-Point', marker='s', linewidth=2)
plt.plot(iters, history_new, label='Newton', marker='x', linewidth=2)
plt.plot(iters, history_sec, label='Secant', marker='^', linewidth=2)

plt.axhline(y=2.0, color='r', linestyle='--', label='Root (x=2.0)')

plt.title('How values of X converge to the root 2.0')
plt.xlabel('Iteration Number')
plt.ylabel('Value of X')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()