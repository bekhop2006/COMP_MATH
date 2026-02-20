
def weddle_rule(x_nodes, y_nodes):
    """Weddle's rule: ∫f ≈ (3h/10)[y_0 + 5y_1 + y_2 + 6y_3 + y_4 + 5y_5 + y_6]"""
    # Проверка: правило Уэддла требует ровно 7 точек (6 интервалов)
    n = len(y_nodes)
    if n != 7:
        raise ValueError("Weddle's rule requires exactly 7 points (6 intervals)")

    # Шаг h — расстояние между соседними узлами
    h = x_nodes[1] - x_nodes[0]

    # Коэффициенты формулы: 1, 5, 1, 6, 1, 5, 1
    coeffs = [1, 5, 1, 6, 1, 5, 1]

    # Взвешенная сумма и итоговый интеграл = (3h/10) * сумма
    result = sum(c * y for c, y in zip(coeffs, y_nodes))
    return (3 * h / 10) * result


# Демонстрация работы метода (запускается при прямом вызове файла)
if __name__ == "__main__":
    # Тестовые данные: y = x² + 1, 7 точек (6 интервалов)
    x_simp = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    y_simp = [2.0, 3.25, 5.0, 7.25, 10.0, 13.25, 17.0]

    # Вывод заголовка и входных данных
    print("--- 2.6 Weddle's Rule ---")
    print(f"Data: x = {x_simp}, y = {y_simp}")

    # Вычисление интеграла и вывод результата
    result = weddle_rule(x_simp, y_simp)
    print(f"∫f dx ≈ {result:.6f}")
    print("True value: 24.0")
