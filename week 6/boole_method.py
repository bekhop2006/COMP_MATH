
# --- ФУНКЦИЯ ВЫЧИСЛЕНИЯ ИНТЕГРАЛА ---
def boole_rule(x_nodes, y_nodes):
    """Boole's rule: ∫f ≈ (2h/45)[7y_0 + 32y_1 + 12y_2 + 32y_3 + 7y_4]"""
    # Проверка: правило Буля требует ровно 5 точек (4 интервала)
    n = len(y_nodes)
    if n != 5:
        raise ValueError("Boole's rule requires exactly 5 points (4 intervals)")

    # Шаг h — расстояние между соседними узлами (равномерная сетка)
    h = x_nodes[1] - x_nodes[0]

    # Коэффициенты формулы: 7, 32, 12, 32, 7 — веса для каждой точки
    coeffs = [7, 32, 12, 32, 7]

    # Взвешенная сумма: Σ(c_i * y_i)
    result = sum(c * y for c, y in zip(coeffs, y_nodes))

    # Итоговый интеграл = (2h/45) * взвешенная сумма
    return (2 * h / 45) * result

∫
# Демонстрация работы метода (запускается при прямом вызове файла)
if __name__ == "__main__":
    # Тестовые данные: y = x² + 1, ∫(x²+1)dx от 1 до 4 = 24
    x_boole = [1.0, 1.75, 2.5, 3.25, 4.0]
    y_boole = [2.0, 4.0625, 7.25, 11.5625, 17.0]

    # Вывод заголовка и входных данных
    print("--- 2.5 Boole's Rule ---")
    print(f"Data: x = {x_boole}, y = {y_boole}")

    # Вычисление интеграла и вывод результата
    result = boole_rule(x_boole, y_boole)
    print(f"∫f dx ≈ {result:.6f}")
    print("True value: 24.0")
