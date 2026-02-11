# Week 5 — Numerical Differentiation

## Как запустить

### 1. Запуск каждого метода отдельно

```bash
cd "week 5"

# Метод Ньютона (forward) — производная в начале таблицы
python3 newton_forward_method.py

# Метод Ньютона (backward) — производная в конце таблицы
python3 newton_backward_method.py

# Неравномерная сетка (forward)
python3 unequally_forward_method.py

# Неравномерная сетка (backward)
python3 unequally_backward_method.py

# Анализ табличной функции (экстремумы)
python3 tabulated_analysis_method.py
```

### 2. Запуск всех методов сразу

```bash
python3 all_methods.py
```

### 3. Тестирование через run_tests.py

```bash
# Все тесты
python3 run_tests.py

# Один метод (1–5)
python3 run_tests.py 1   # newton_forward
python3 run_tests.py 2   # newton_backward
python3 run_tests.py 3   # unequally_forward
python3 run_tests.py 4   # unequally_backward
python3 run_tests.py 5   # tabulated_analysis
```

## Использование в своём коде

```python
from newton_forward_method import derivative_newton_forward
from newton_backward_method import derivative_newton_backward
from unequally_forward_method import derivative_unequally_forward
from unequally_backward_method import derivative_unequally_backward
from tabulated_analysis_method import find_maxima_minima

# Равномерная сетка
x = [1.0, 2.0, 3.0, 4.0, 5.0]
y = [2.0, 5.0, 10.0, 17.0, 26.0]

df_start = derivative_newton_forward(x, y)   # f'(x_0)
df_end = derivative_newton_backward(x, y)     # f'(x_n)

# Неравномерная сетка
x_u = [1.0, 1.5, 2.5, 4.0, 5.0]
y_u = [2.0, 3.25, 7.25, 17.0, 26.0]

df_fwd = derivative_unequally_forward(x_u, y_u)
df_bwd = derivative_unequally_backward(x_u, y_u)

# Поиск экстремумов
extrema, d1, d2 = find_maxima_minima(x, y)
for x_val, y_val, kind, fpp in extrema:
    print(f"At x={x_val}: {kind} (f''={fpp})")
```

## Файлы

| Файл | Описание |
|------|----------|
| `newton_forward_method.py` | 2.1 Newton's Forward Difference |
| `newton_backward_method.py` | 2.2 Newton's Backward Difference |
| `unequally_forward_method.py` | 3.1 Unequally Spaced Forward |
| `unequally_backward_method.py` | 3.2 Unequally Spaced Backward |
| `tabulated_analysis_method.py` | 4. Maxima/Minima Analysis |
| `all_methods.py` | Все методы в одном файле |
| `run_tests.py` | Скрипт тестирования |
