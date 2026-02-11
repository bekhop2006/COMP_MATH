# 3.1 Unequally Spaced Forward Difference (Numerical Differentiation)
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

    # P'(x_0) = f[x_0,x_1] + (x_0-x_1)f[x_0,x_1,x_2] + (x_0-x_1)(x_0-x_2)f[x_0,x_1,x_2,x_3] + ...
    result = dd[0][1]  # f[x_0, x_1]
    for k in range(2, n):
        term = dd[0][k]
        for j in range(1, k):
            term *= (x_nodes[0] - x_nodes[j])
        result += term
    return result


if __name__ == "__main__":
    # Demo: y = x^2 + 1, f'(x) = 2x (неравномерная сетка)
    x_uneq = [1.0, 1.5, 2.5, 4.0, 5.0]
    y_uneq = [2.0, 3.25, 7.25, 17.0, 26.0]

    print("--- Unequally Spaced Forward Difference ---")
    print(f"Data: x = {x_uneq}, y = {y_uneq}")
    df = derivative_unequally_forward(x_uneq, y_uneq)
    print(f"f'(x_0) at x_0 = {x_uneq[0]}: {df:.4f}")
    print(f"True value (2*x_0): {2 * x_uneq[0]:.4f}")
