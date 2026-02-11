# CHAPTER 3 — NUMERICAL DIFFERENTIATION
# Все методы численного дифференцирования в одном файле (аналогично week 2, week 4)

# --- 1. GENERAL DESCRIPTION ---
# Численное дифференцирование — приближённое вычисление производных по табличным данным
# или дискретным значениям функции, когда аналитическая формула неизвестна.

# Общие данные: равномерная сетка (equally spaced)
x_eq = [1.0, 2.0, 3.0, 4.0]
y_eq = [2.0, 4.0, 7.0, 11.0]   # y = x^2 + 1
n_eq = len(x_eq)
h_eq = x_eq[1] - x_eq[0]

# Неравномерная сетка (unequally spaced)
x_uneq = [1.0, 1.5, 2.5, 4.0, 5.0]
y_uneq = [2.0, 3.25, 7.25, 17.0, 26.0]  # y = x^2 + 1
n_uneq = len(x_uneq)


def build_forward_diff_table(y):
    """Таблица конечных разностей (forward differences Δ^k y_0)"""
    n = len(y)
    diff = [list(y)]
    for k in range(1, n):
        row = [diff[k - 1][i + 1] - diff[k - 1][i] for i in range(n - k)]
        diff.append(row)
    return diff


def build_backward_diff_table(y):
    """Таблица конечных разностей (backward differences ∇^k y_n)"""
    n = len(y)
    diff = [list(y)]
    for k in range(1, n):
        row = [diff[k - 1][i + 1] - diff[k - 1][i] for i in range(n - k)]
        diff.append(row)
    return diff  # ∇^k y_n = Δ^k y_{n-k} (то же самое, но берём последний столбец)


# --- 2.1 NEWTON'S FORWARD DIFFERENCE FORMULA (equally spaced) ---
# f'(x_0) = (1/h)[Δy_0 - Δ²y_0/2 + Δ³y_0/3 - Δ⁴y_0/4 + ...]
# Производная в начале таблицы

def derivative_newton_forward(x_nodes, y_nodes, index=0):
    """Первая производная в точке x_index по формуле Ньютона (forward)"""
    n = len(y_nodes)
    h = x_nodes[1] - x_nodes[0]
    diff = build_forward_diff_table(y_nodes)

    # f'(x_0) = (1/h) * sum_{k=1}^{n-1} (-1)^{k+1} * Δ^k y_0 / k
    result = 0.0
    for k in range(1, n):
        sign = (-1) ** (k + 1)
        result += sign * diff[k][index] / k
    return result / h


print("\n--- 2.1 NEWTON'S FORWARD DIFFERENCE (derivative) ---")
df_forward = derivative_newton_forward(x_eq, y_eq)
print(f"Data: x = {x_eq}, y = {y_eq}")
print(f"f'(x_0) at x_0 = {x_eq[0]}: {df_forward:.4f}")
print(f"True (2*x_0): {2 * x_eq[0]:.4f}")


# --- 2.2 NEWTON'S BACKWARD DIFFERENCE FORMULA (equally spaced) ---
# f'(x_n) = (1/h)[∇y_n + ∇²y_n/2 + ∇³y_n/3 + ...]
# Производная в конце таблицы

def derivative_newton_backward(x_nodes, y_nodes, index=-1):
    """Первая производная в точке x_index по формуле Ньютона (backward)"""
    n = len(y_nodes)
    h = x_nodes[1] - x_nodes[0]
    diff = build_backward_diff_table(y_nodes)

    # f'(x_n) = (1/h) * sum_{k=1}^{n-1} ∇^k y_n / k
    # ∇^k y_n = Δ^k y_{n-k} = diff[k][n-1-k]
    result = 0.0
    for k in range(1, n):
        if n - 1 - k >= 0:
            result += diff[k][n - 1 - k] / k
    return result / h


print("\n--- 2.2 NEWTON'S BACKWARD DIFFERENCE (derivative) ---")
df_backward = derivative_newton_backward(x_eq, y_eq)
print(f"f'(x_n) at x_n = {x_eq[-1]}: {df_backward:.4f}")
print(f"True (2*x_n): {2 * x_eq[-1]:.4f}")


# --- 3.1 UNEQUALLY SPACED FORWARD DIFFERENCE ---
# Используем полином Ньютона с разделёнными разностями, дифференцируем и вычисляем в x_0

def divided_differences(x_nodes, y_nodes):
    """Таблица разделённых разностей f[x_i, x_{i+1}, ..., x_{i+j}]"""
    n = len(x_nodes)
    dd = [[0.0] * n for _ in range(n)]
    for i in range(n):
        dd[i][0] = y_nodes[i]
    for j in range(1, n):
        for i in range(n - j):
            dd[i][j] = (dd[i + 1][j - 1] - dd[i][j - 1]) / (x_nodes[i + j] - x_nodes[i])
    return dd


def derivative_unequally_forward(x_nodes, y_nodes):
    """Первая производная в x_0 (неравномерная сетка, forward)"""
    n = len(x_nodes)
    dd = divided_differences(x_nodes, y_nodes)

    # P(x) = f[x_0] + (x-x_0)f[x_0,x_1] + (x-x_0)(x-x_1)f[x_0,x_1,x_2] + ...
    # P'(x) = f[x_0,x_1] + [(x-x_1)+(x-x_0)]f[x_0,x_1,x_2] + ...
    # P'(x_0) = f[x_0,x_1] + (x_0-x_1)f[x_0,x_1,x_2] + (x_0-x_1)(x_0-x_2)f[x_0,x_1,x_2,x_3] + ...
    result = dd[0][1]  # f[x_0, x_1]
    for k in range(2, n):
        term = dd[0][k]
        for j in range(1, k):
            term *= (x_nodes[0] - x_nodes[j])
        result += term
    return result


print("\n--- 3.1 UNEQUALLY SPACED FORWARD DIFFERENCE ---")
print(f"Data: x = {x_uneq}, y = {y_uneq}")
df_uneq_fwd = derivative_unequally_forward(x_uneq, y_uneq)
print(f"f'(x_0) at x_0 = {x_uneq[0]}: {df_uneq_fwd:.4f}")
print(f"True (2*x_0): {2 * x_uneq[0]:.4f}")


# --- 3.2 UNEQUALLY SPACED BACKWARD DIFFERENCE ---
# Производная в x_n (последняя точка), используем обратный порядок узлов

def derivative_unequally_backward(x_nodes, y_nodes):
    """Первая производная в x_n (неравномерная сетка, backward)"""
    n = len(x_nodes)
    # Обратный порядок: x_n, x_{n-1}, ..., x_0
    x_rev = list(reversed(x_nodes))
    y_rev = list(reversed(y_nodes))
    dd = divided_differences(x_rev, y_rev)

    # P'(x_n) при x_n = x_rev[0]
    result = dd[0][1]
    for k in range(2, n):
        term = dd[0][k]
        for j in range(1, k):
            term *= (x_rev[0] - x_rev[j])
        result += term
    return result


print("\n--- 3.2 UNEQUALLY SPACED BACKWARD DIFFERENCE ---")
df_uneq_bwd = derivative_unequally_backward(x_uneq, y_uneq)
print(f"f'(x_n) at x_n = {x_uneq[-1]}: {df_uneq_bwd:.4f}")
print(f"True (2*x_n): {2 * x_uneq[-1]:.4f}")


# --- 4. ANALYSIS OF TABULATED FUNCTIONS ---
# 4.1 Maxima and Minima of a tabulated function
# 4.2 First derivative test for Maxima and Minima
# 4.3 Second derivative test for Maxima and Minima

def derivative_at_point_central(x_nodes, y_nodes, i):
    """Центральная разность для производной в точке i (если есть соседи)"""
    if i <= 0:
        return (y_nodes[1] - y_nodes[0]) / (x_nodes[1] - x_nodes[0])
    if i >= len(x_nodes) - 1:
        return (y_nodes[-1] - y_nodes[-2]) / (x_nodes[-1] - x_nodes[-2])
    h = x_nodes[i + 1] - x_nodes[i]
    return (y_nodes[i + 1] - y_nodes[i - 1]) / (x_nodes[i + 1] - x_nodes[i - 1])


def second_derivative_at_point(x_nodes, y_nodes, i):
    """Вторая производная: f''(x) ≈ (f(x+h) - 2f(x) + f(x-h)) / h^2"""
    if i <= 0 or i >= len(x_nodes) - 1:
        return 0.0
    h = x_nodes[i + 1] - x_nodes[i]
    return (y_nodes[i + 1] - 2 * y_nodes[i] + y_nodes[i - 1]) / (h ** 2)


def find_maxima_minima(x_nodes, y_nodes):
    """
    4.1 Maxima and Minima of a tabulated function
    4.2 First derivative test: f' меняет знак с + на - → max; с - на + → min
    4.3 Second derivative test: f'' < 0 → max; f'' > 0 → min
    """
    n = len(x_nodes)
    derivatives = [derivative_at_point_central(x_nodes, y_nodes, i) for i in range(n)]
    second_derivatives = [second_derivative_at_point(x_nodes, y_nodes, i) for i in range(n)]

    extrema = []
    for i in range(1, n - 1):
        # First derivative test: sign change
        d_left = derivatives[i - 1]
        d_right = derivatives[i + 1]
        d_curr = derivatives[i]

        # Approximate: derivative crosses zero between points
        if (d_left > 0 and d_right < 0) or (d_left < 0 and d_right > 0):
            # Second derivative test
            fpp = second_derivatives[i]
            if fpp < 0:
                extrema.append((x_nodes[i], y_nodes[i], "maximum", fpp))
            elif fpp > 0:
                extrema.append((x_nodes[i], y_nodes[i], "minimum", fpp))
            else:
                extrema.append((x_nodes[i], y_nodes[i], "saddle/inconclusive", second_derivatives[i]))

    return extrema, derivatives, second_derivatives


print("\n--- 4. ANALYSIS OF TABULATED FUNCTIONS ---")
# Данные с экстремумом: y = (x-3)^2 + 1 — минимум при x=3
x_tab = [1.0, 2.0, 3.0, 4.0, 5.0]
y_tab = [5.0, 2.0, 1.0, 2.0, 5.0]  # парабола, минимум в x=3

extrema, d1, d2 = find_maxima_minima(x_tab, y_tab)
print("4.1 Maxima and Minima:")
print(f"  Data: x = {x_tab}, y = {y_tab}")
print(f"  First derivatives (approx): {[round(d, 4) for d in d1]}")
print(f"  Second derivatives (approx):  {[round(d, 4) for d in d2]}")
print("4.2 & 4.3 Extrema found:")
for x, y, kind, fpp in extrema:
    print(f"  At x = {x}: y = {y} — {kind} (f'' = {fpp:.4f})")


# --- SUMMARY ---
print("\n--- SUMMARY (Numerical Differentiation) ---")
print(f"Newton forward (at x_0):     {df_forward:.4f}")
print(f"Newton backward (at x_n):   {df_backward:.4f}")
print(f"Unequally forward (at x_0): {df_uneq_fwd:.4f}")
print(f"Unequally backward (at x_n): {df_uneq_bwd:.4f}")
print(f"Extrema: {len(extrema)} found")
