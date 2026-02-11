# 3.2 Unequally Spaced Backward Difference (Numerical Differentiation)
# Производная в x_n (последняя точка), используем обратный порядок узлов


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


def derivative_unequally_backward(x_nodes, y_nodes):
    """Первая производная в x_n (неравномерная сетка, backward)"""
    n = len(x_nodes)
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


if __name__ == "__main__":
    # Demo: y = x^2 + 1, f'(x) = 2x (неравномерная сетка)
    x_uneq = [1.0, 1.5, 2.5, 4.0, 5.0]
    y_uneq = [2.0, 3.25, 7.25, 17.0, 26.0]

    print("--- Unequally Spaced Backward Difference ---")
    print(f"Data: x = {x_uneq}, y = {y_uneq}")
    df = derivative_unequally_backward(x_uneq, y_uneq)
    print(f"f'(x_n) at x_n = {x_uneq[-1]}: {df:.4f}")
    print(f"True value (2*x_n): {2 * x_uneq[-1]:.4f}")
