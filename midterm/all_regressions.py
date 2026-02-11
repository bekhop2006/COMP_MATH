import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 1. y = Ax + B
def linear_func(x, A, B):
    return A * x + B

# 2. y = ax² + bx + c
def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# 3. y = a^(bx)
def exp_base_a_func(x, a, b):
    return a ** (b * x)

# 4. y = a*log(bx)
def log_func(x, a, b):
    return a * np.log(b * x)

# 5. y = a*e^(bx)
def exp_e_func(x, a, b):
    return a * np.exp(b * x)

# Пример данных для всех функций
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("=" * 60)
print("РЕГРЕССИОННЫЙ АНАЛИЗ")
print("=" * 60)

# 1. Линейная регрессия
y1 = np.array([2.5, 4.8, 6.9, 9.1, 11.2, 13.5, 15.6, 17.8, 20.0, 22.1])
params1, _ = curve_fit(linear_func, x_data, y1)
A, B = params1
print(f"\n1. y = Ax + B")
print(f"   A = {A:.4f}, B = {B:.4f}")
print(f"   y = {A:.4f}x + {B:.4f}")

# 2. Квадратичная регрессия
y2 = np.array([2.1, 5.2, 10.3, 17.4, 26.5, 37.6, 50.7, 65.8, 82.9, 102.0])
params2, _ = curve_fit(quadratic_func, x_data, y2)
a, b, c = params2
print(f"\n2. y = ax² + bx + c")
print(f"   a = {a:.4f}, b = {b:.4f}, c = {c:.4f}")
print(f"   y = {a:.4f}x² + {b:.4f}x + {c:.4f}")

# 3. Экспоненциальная (a^bx)
y3 = np.array([2.5, 6.25, 15.6, 39.1, 97.7, 244.1, 610.4, 1525.9, 3814.7, 9536.7])
params3, _ = curve_fit(exp_base_a_func, x_data, y3, p0=[2.5, 1.0])
a3, b3 = params3
print(f"\n3. y = a^(bx)")
print(f"   a = {a3:.4f}, b = {b3:.4f}")
print(f"   y = {a3:.4f}^({b3:.4f}x)")

# 4. Логарифмическая
y4 = np.array([0.5, 1.7, 2.6, 3.3, 3.9, 4.4, 4.8, 5.2, 5.5, 5.8])
params4, _ = curve_fit(log_func, x_data, y4, p0=[2.0, 1.0])
a4, b4 = params4
print(f"\n4. y = a*log(bx)")
print(f"   a = {a4:.4f}, b = {b4:.4f}")
print(f"   y = {a4:.4f}*log({b4:.4f}*x)")

# 5. Экспоненциальная (e^bx)
y5 = np.array([5.4, 14.8, 40.2, 109.2, 296.8, 806.9, 2194.0, 5957.0, 16181.0, 43980.0])
params5, _ = curve_fit(exp_e_func, x_data, y5, p0=[2.0, 1.0])
a5, b5 = params5
print(f"\n5. y = a*e^(bx)")
print(f"   a = {a5:.4f}, b = {b5:.4f}")
print(f"   y = {a5:.4f}*e^({b5:.4f}*x)")

print("\n" + "=" * 60)
