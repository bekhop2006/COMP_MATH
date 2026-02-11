import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# y = a^(bx)
def exp_base_a_func(x, a, b):
    return a ** (b * x)

# Пример данных
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([2.5, 6.25, 15.6, 39.1, 97.7, 244.1, 610.4, 1525.9, 3814.7, 9536.7])

# Подгонка параметров
params, _ = curve_fit(exp_base_a_func, x_data, y_data, p0=[2.5, 1.0])
a, b = params

print("Экспоненциальная регрессия: y = a^(bx)")
print("=" * 40)
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")
print(f"\nУравнение: y = {a:.4f}^({b:.4f}x)")

# Предсказание
y_pred = exp_base_a_func(x_data, a, b)
print(f"\nПредсказанные значения:")
for i in range(len(x_data)):
    print(f"x={x_data[i]:.1f}, y_реальное={y_data[i]:.2f}, y_предсказанное={y_pred[i]:.2f}")

# График
x_plot = np.linspace(x_data.min(), x_data.max(), 100)
y_plot = exp_base_a_func(x_plot, a, b)

plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, color='red', label='Данные', s=50)
plt.plot(x_plot, y_plot, 'b-', label=f'y = {a:.4f}^({b:.4f}x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Экспоненциальная регрессия: y = a^(bx)')
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.show()
