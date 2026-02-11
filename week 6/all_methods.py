# CHAPTER 4 — NUMERICAL INTEGRATION
# Все методы численного интегрирования (импорт из отдельных файлов)
# Запуск: python3 all_methods.py — выводит сводную таблицу по всем методам


# --- ТЕСТОВЫЕ ДАННЫЕ ---
# y = x² + 1, ∫(x²+1)dx от 1 до 4 = 24

# Для трапеций: 4 точки (3 интервала)
x_eq = [1.0, 2.0, 3.0, 4.0]
y_eq = [2.0, 4.0, 7.0, 11.0]

# Для Simpson 1/3 и Weddle: 7 точек (6 интервалов)
x_simp = [1.0, 1.1, 1.2, 2.5, 3.0, 3.5, 4.0]
y_simp = [2.0, 3.25, 5.0, 7.25, 10.0, 13.25, 17.0]

# Для Simpson 3/8: 4 точки (3 интервала)
x_38 = [1.0, 2.0, 3.0, 4.0]
y_38 = [2.0, 4.0, 7.0, 11.0]

# Для Boole: 5 точек (4 интервала)
x_boole = [1.0, 1.75, 2.5, 3.25, 4.0]
y_boole = [2.0, 4.0625, 7.25, 11.5625, 17.0]


# --- ИМПОРТ ФУНКЦИЙ ИЗ ОТДЕЛЬНЫХ МОДУЛЕЙ ---
from trapezoidal_method import trapezoidal_rule
from simpson_one_third_method import simpson_one_third
from simpson_three_eighth_method import simpson_three_eighth
from boole_method import boole_rule
from weddle_method import weddle_rule


# --- ЗАПУСК ВСЕХ МЕТОДОВ И ВЫВОД СВОДКИ ---
if __name__ == "__main__":
    # Вычисляем интеграл каждым методом
    trap = trapezoidal_rule(x_eq, y_eq)
    simp_13 = simpson_one_third(x_simp, y_simp)
    simp_38 = simpson_three_eighth(x_38, y_38)
    boole_val = boole_rule(x_boole, y_boole)
    weddle_val = weddle_rule(x_simp, y_simp)

    # Выводим сравнительную таблицу результатов
    print("\n--- SUMMARY (Numerical Integration) ---")
    print(f"Trapezoidal:    {trap:.6f}")
    print(f"Simpson 1/3:    {simp_13:.6f}")
    print(f"Simpson 3/8:    {simp_38:.6f}")
    print(f"Boole:          {boole_val:.6f}")
    print(f"Weddle:         {weddle_val:.6f}")
    print(f"True value:     24.0")
