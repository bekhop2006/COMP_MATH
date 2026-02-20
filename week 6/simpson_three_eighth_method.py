

# --- ФУНКЦИЯ ВЫЧИСЛЕНИЯ ИНТЕГРАЛА ---
def simpson_three_eighth(x_nodes, y_nodes):
    """Simpson's 3/8 rule: ∫f ≈ (3h/8)[y_0 + 3y_1 + 3y_2 + 2y_3 + 3y_4 + ...]"""
    # Проверка: число интервалов должно быть кратно 3
    n = len(y_nodes)
    if (n - 1) % 3 != 0:
        raise ValueError("Simpson 3/8 needs (n-1) divisible by 3 intervals")

    # Шаг h — расстояние между соседними узлами
    h = x_nodes[1] - x_nodes[0]

    # Формируем коэффициенты: концы — 1, стыки групп (i кратно 3) — 2, остальные внутренние — 3
    coeffs = []
    for i in range(n):
        if i % 3 == 0 and i > 0 and i < n - 1:
            coeffs.append(2)
        else:
            coeffs.append(3 if 0 < i < n - 1 else 1)

    # Взвешенная сумма и итоговый интеграл = (3h/8) * сумма
    result = sum(c * y for c, y in zip(coeffs, y_nodes))
    return (3 * h / 8) * result


# Демонстрация работы метода (запускается при прямом вызове файла)
if __name__ == "__main__":
    # Тестовые данные: y = x² + 1, 4 точки (3 интервала)
    x_38 = [1.0, 2.0, 3.0, 4.0]
    y_38 = [2.0, 4.0, 7.0, 11.0]

    # Вывод заголовка и входных данных
    print("--- 2.4 Simpson's Three-Eighth Rule ---")
    print(f"Data: x = {x_38}, y = {y_38}")

    # Вычисление интеграла и вывод результата
    result = simpson_three_eighth(x_38, y_38)
    print(f"∫f dx ≈ {result:.6f}")
    print("True value: 24.0")
