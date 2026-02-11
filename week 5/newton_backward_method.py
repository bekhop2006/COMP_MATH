# 2.2 Newton's Backward Difference Formula (Numerical Differentiation)
# f'(x_n) = (1/h)[∇y_n + ∇²y_n/2 + ∇³y_n/3 + ...]
# Производная в конце таблицы (equally spaced)


def build_backward_diff_table(y):
    """Таблица конечных разностей (backward: ∇^k y_n = Δ^k y_{n-k})"""
    n = len(y)
    diff = [list(y)]
    for k in range(1, n):
        row = [diff[k - 1][i + 1] - diff[k - 1][i] for i in range(n - k)]
        diff.append(row)
    return diff


def derivative_newton_backward(x_nodes, y_nodes):
    """Первая производная в последней точке x_n по формуле Ньютона (backward)"""
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


if __name__ == "__main__":
    # Demo: y = x^2 + 1, f'(x) = 2x
    x_eq = [1.0, 2.0, 3.0, 4.0, 5.0]
    y_eq = [2.0, 5.0, 10.0, 17.0, 26.0]

    print("--- Newton's Backward Difference Formula ---")
    print(f"Data: x = {x_eq}, y = {y_eq}")
    df = derivative_newton_backward(x_eq, y_eq)
    print(f"f'(x_n) at x_n = {x_eq[-1]}: {df:.4f}")
    print(f"True value (2*x_n): {2 * x_eq[-1]:.4f}")
