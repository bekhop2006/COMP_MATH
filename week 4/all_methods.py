# CHAPTER 2 — INTERPOLATION
# Все методы интерполяции в одном файле (аналогично week 2)
import copy

# Общие данные: узлы (x) и значения (y)
x_data = [1.0, 2.0, 3.0, 4.0, 5.0]
y_data = [2.0, 5.0, 10.0, 17.0, 26.0]   # y = x^2 + 1
n = len(x_data)

# Точка, в которой вычисляем интерполянт
x_eval = 2.5


# --- 2.1 LAGRANGE'S INTERPOLATION FORMULA ---
# P(x) = sum over i of y_i * L_i(x), где L_i(x) = prod_{j!=i} (x - x_j)/(x_i - x_j)

def lagrange_interpolate(x_nodes, y_nodes, x):
    result = 0.0
    n = len(x_nodes)
    for i in range(n):
        term = y_nodes[i]
        for j in range(n):
            if j != i:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result


print("\n--- 2.1 LAGRANGE'S INTERPOLATION ---")
y_lagrange = lagrange_interpolate(x_data, y_data, x_eval)
print(f"Data: x = {x_data}, y = {y_data}")
print(f"At x = {x_eval}: P(x) = {y_lagrange:.4f}")


# --- 2.2 NEWTON'S FORWARD INTERPOLATION FORMULA ---
# Для равномерной сетки: h = x_{i+1} - x_i, u = (x - x_0)/h
# P_n(x) = y_0 + u*Δy_0 + u(u-1)/2!*Δ²y_0 + ...

def newton_forward(x_nodes, y_nodes, x):
    n = len(x_nodes)
    h = x_nodes[1] - x_nodes[0]
    u = (x - x_nodes[0]) / h

    # Таблица конечных разностей (forward differences)
    diff = [list(y_nodes)]
    for k in range(1, n):
        row = []
        for i in range(n - k):
            row.append(diff[k - 1][i + 1] - diff[k - 1][i])
        diff.append(row)

    result = diff[0][0]
    term = 1.0
    for k in range(1, n):
        term *= (u - (k - 1)) / k
        result += term * diff[k][0]
    return result


print("\n--- 2.2 NEWTON'S FORWARD INTERPOLATION ---")
y_forward = newton_forward(x_data, y_data, x_eval)
print(f"At x = {x_eval}: P(x) = {y_forward:.4f}")


# --- 2.3 NEWTON'S BACKWARD INTERPOLATION FORMULA ---
# u = (x - x_n)/h, P_n(x) = y_n + u*∇y_n + u(u+1)/2!*∇²y_n + ...

def newton_backward(x_nodes, y_nodes, x):
    n = len(x_nodes)
    h = x_nodes[1] - x_nodes[0]
    u = (x - x_nodes[-1]) / h

    # Таблица конечных разностей (backward — используем те же diff, но берём последний столбец)
    diff = [list(y_nodes)]
    for k in range(1, n):
        row = []
        for i in range(n - k):
            row.append(diff[k - 1][i + 1] - diff[k - 1][i])
        diff.append(row)

    result = diff[0][-1]  # y_n
    term = 1.0
    for k in range(1, n):
        term *= (u + (k - 1)) / k
        result += term * diff[k][-1]
    return result


print("\n--- 2.3 NEWTON'S BACKWARD INTERPOLATION ---")
y_backward = newton_backward(x_data, y_data, x_eval)
print(f"At x = {x_eval}: P(x) = {y_backward:.4f}")


# --- 2.4 NEWTON'S DIVIDED DIFFERENCE FORMULA ---
# P(x) = f[x_0] + (x-x_0)f[x_0,x_1] + (x-x_0)(x-x_1)f[x_0,x_1,x_2] + ...

def divided_differences(x_nodes, y_nodes):
    n = len(x_nodes)
    # dd[i][j] = f[x_i, x_{i+1}, ..., x_{i+j}]
    dd = [[0.0] * n for _ in range(n)]
    for i in range(n):
        dd[i][0] = y_nodes[i]
    for j in range(1, n):
        for i in range(n - j):
            dd[i][j] = (dd[i + 1][j - 1] - dd[i][j - 1]) / (x_nodes[i + j] - x_nodes[i])
    return dd


def newton_divided_difference(x_nodes, y_nodes, x):
    n = len(x_nodes)
    dd = divided_differences(x_nodes, y_nodes)
    result = dd[0][0]
    product = 1.0
    for k in range(1, n):
        product *= (x - x_nodes[k - 1])
        result += product * dd[0][k]
    return result


print("\n--- 2.4 NEWTON'S DIVIDED DIFFERENCE ---")
y_dd = newton_divided_difference(x_data, y_data, x_eval)
print(f"At x = {x_eval}: P(x) = {y_dd:.4f}")


# --- 2.5 SPLINE INTERPOLATION (Cubic Spline) ---
# На каждом отрезке [x_i, x_{i+1}] кубический полином S_i(x).
# Условия: совпадение в узлах, непрерывность 1-й и 2-й производных, краевые условия (natural: M_0 = M_n = 0).

def cubic_spline_coefficients(x_nodes, y_nodes):
    n = len(x_nodes)
    h = [x_nodes[i + 1] - x_nodes[i] for i in range(n - 1)]

    # Трёхдиагональная система для вторых производных M_i
    # 2*M_0 = 0, 2*M_n = 0 (natural spline)
    # Для внутренних: h_{i-1}*M_{i-1} + 2(h_{i-1}+h_i)*M_i + h_i*M_{i+1} = 6*((y_{i+1}-y_i)/h_i - (y_i-y_{i-1})/h_{i-1})
    A = [[0.0] * n for _ in range(n)]
    b = [0.0] * n

    A[0][0] = 1.0
    A[n - 1][n - 1] = 1.0

    for i in range(1, n - 1):
        A[i][i - 1] = h[i - 1]
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        b[i] = 6 * ((y_nodes[i + 1] - y_nodes[i]) / h[i] - (y_nodes[i] - y_nodes[i - 1]) / h[i - 1])

    # Решаем систему (прогонка или простой Gauss)
    M = solve_tridiagonal(A, b)

    # Коэффициенты для каждого отрезка: S_i(x) = a_i + b_i*(x-x_i) + c_i*(x-x_i)^2 + d_i*(x-x_i)^3
    coeffs = []
    for i in range(n - 1):
        a_i = y_nodes[i]
        c_i = M[i] / 2
        d_i = (M[i + 1] - M[i]) / (6 * h[i])
        b_i = (y_nodes[i + 1] - y_nodes[i]) / h[i] - h[i] * (2 * M[i] + M[i + 1]) / 6
        coeffs.append((a_i, b_i, c_i, d_i))
    return x_nodes, coeffs, h


def solve_tridiagonal(A_in, b_in):
    A = copy.deepcopy(A_in)
    b = copy.deepcopy(b_in)
    n = len(b)
    x = [0.0] * n
    for i in range(n):
        pivot = A[i][i]
        if abs(pivot) < 1e-12:
            pivot = 1e-12
        for j in range(n):
            A[i][j] /= pivot
        b[i] /= pivot
        if i < n - 1:
            factor = A[i + 1][i]
            for j in range(n):
                A[i + 1][j] -= factor * A[i][j]
            b[i + 1] -= factor * b[i]
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
    return x


def spline_evaluate(x_nodes, coeffs, h_list, x):
    n = len(x_nodes)
    if x <= x_nodes[0]:
        i = 0
    elif x >= x_nodes[-1]:
        i = n - 2
    else:
        for i in range(n - 1):
            if x_nodes[i] <= x <= x_nodes[i + 1]:
                break
    dx = x - x_nodes[i]
    a, b, c, d = coeffs[i]
    return a + b * dx + c * dx ** 2 + d * dx ** 3


print("\n--- 2.5 SPLINE INTERPOLATION (Cubic) ---")
x_nodes_s, coeffs_s, h_s = cubic_spline_coefficients(x_data, y_data)
y_spline = spline_evaluate(x_nodes_s, coeffs_s, h_s, x_eval)
print(f"At x = {x_eval}: S(x) = {y_spline:.4f}")


# --- Сводка ---
print("\n--- SUMMARY (all at x = {}) ---".format(x_eval))
print(f"Lagrange:        {y_lagrange:.4f}")
print(f"Newton forward:  {y_forward:.4f}")
print(f"Newton backward: {y_backward:.4f}")
print(f"Divided diff:    {y_dd:.4f}")
print(f"Cubic spline:    {y_spline:.4f}")
# Для y = x^2 + 1 истинное значение:
true_val = x_eval ** 2 + 1
print(f"True (x^2+1):    {true_val:.4f}")
