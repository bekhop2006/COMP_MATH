import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# y = ax² + bx + c
def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# Пример данных
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([2.1, 5.2, 10.3, 17.4, 26.5, 37.6, 50.7, 65.8, 82.9, 102.0])

# Подгонка параметров
params, _ = curve_fit(quadratic_func, x_data, y_data)
a, b, c = params

print("Квадратичная регрессия: y = ax² + bx + c")
print("=" * 40)
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")
print(f"c = {c:.4f}")
print(f"\nУравнение: y = {a:.4f}x² + {b:.4f}x + {c:.4f}")

# Предсказание
y_pred = quadratic_func(x_data, a, b, c)
print(f"\nПредсказанные значения:")
for i in range(len(x_data)):
    print(f"x={x_data[i]:.1f}, y_реальное={y_data[i]:.2f}, y_предсказанное={y_pred[i]:.2f}")

# График
x_plot = np.linspace(x_data.min(), x_data.max(), 100)
y_plot = quadratic_func(x_plot, a, b, c)

plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, color='red', label='Данные', s=50)
plt.plot(x_plot, y_plot, 'b-', label=f'y = {a:.4f}x² + {b:.4f}x + {c:.4f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Квадратичная регрессия: y = ax² + bx + c')
plt.legend()
plt.grid(True)
plt.show()
