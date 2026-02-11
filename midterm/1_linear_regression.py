import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# y = Ax + B
def linear_func(x, A, B):
    return A * x + B

# Пример данных
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([2.5, 4.8, 6.9, 9.1, 11.2, 13.5, 15.6, 17.8, 20.0, 22.1])

# Подгонка параметров
params, _ = curve_fit(linear_func, x_data, y_data)
A, B = params

print("Линейная регрессия: y = Ax + B")
print("=" * 40)
print(f"A = {A:.4f}")
print(f"B = {B:.4f}")
print(f"\nУравнение: y = {A:.4f}x + {B:.4f}")

# Предсказание
y_pred = linear_func(x_data, A, B)
print(f"\nПредсказанные значения:")
for i in range(len(x_data)):
    print(f"x={x_data[i]:.1f}, y_реальное={y_data[i]:.2f}, y_предсказанное={y_pred[i]:.2f}")

# График
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, color='red', label='Данные', s=50)
plt.plot(x_data, y_pred, 'b-', label=f'y = {A:.4f}x + {B:.4f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Линейная регрессия: y = Ax + B')
plt.legend()
plt.grid(True)
plt.show()
