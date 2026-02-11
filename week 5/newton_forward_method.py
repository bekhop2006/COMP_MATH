# 2.1 Newton's Forward Difference Formula (Numerical Differentiation)
# f'(x_0) = (1/h)[Δy_0 - Δ²y_0/2 + Δ³y_0/3 - Δ⁴y_0/4 + ...]
# Производная в начале таблицы (equally spaced)


def build_forward_diff_table(y):
    """Таблица конечных разностей (forward differences Δ^k y_0)"""
    n = len(y)
    diff = [list(y)]
    for k in range(1, n):
        row = [diff[k - 1][i + 1] - diff[k - 1][i] for i in range(n - k)]
        diff.append(row)
    return diff


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


if __name__ == "__main__":
    # Demo: y = x^2 + 1, f'(x) = 2x
    x_eq = [1.0, 2.0, 3.0, 4.0, 5.0]
    y_eq = [2.0, 5.0, 10.0, 17.0, 26.0]

    print("--- Newton's Forward Difference Formula ---")
    print(f"Data: x = {x_eq}, y = {y_eq}")
    df = derivative_newton_forward(x_eq, y_eq)
    print(f"f'(x_0) at x_0 = {x_eq[0]}: {df:.4f}")
    print(f"True value (2*x_0): {2 * x_eq[0]:.4f}")
