import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# y = a*log(bx)
def log_func(x, a, b):
    return a * np.log(b * x)

# Пример данных (x должен быть > 0)
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([0.5, 1.7, 2.6, 3.3, 3.9, 4.4, 4.8, 5.2, 5.5, 5.8])

# Подгонка параметров
params, _ = curve_fit(log_func, x_data, y_data, p0=[2.0, 1.0])
a, b = params

print("Логарифмическая регрессия: y = a*log(bx)")
print("=" * 40)
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")
print(f"\nУравнение: y = {a:.4f}*log({b:.4f}*x)")

# Предсказание
y_pred = log_func(x_data, a, b)
print(f"\nПредсказанные значения:")
for i in range(len(x_data)):
    print(f"x={x_data[i]:.1f}, y_реальное={y_data[i]:.2f}, y_предсказанное={y_pred[i]:.2f}")

# График
x_plot = np.linspace(x_data.min(), x_data.max(), 100)
y_plot = log_func(x_plot, a, b)

plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, color='red', label='Данные', s=50)
plt.plot(x_plot, y_plot, 'b-', label=f'y = {a:.4f}*log({b:.4f}*x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Логарифмическая регрессия: y = a*log(bx)')
plt.legend()
plt.grid(True)
plt.show()
