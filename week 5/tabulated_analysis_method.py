# 4. Analysis of Tabulated Functions
# 4.1 Maxima and Minima of a tabulated function
# 4.2 First derivative test for Maxima and Minima
# 4.3 Second derivative test for Maxima and Minima


def derivative_at_point_central(x_nodes, y_nodes, i):
    """Центральная разность для производной в точке i"""
    if i <= 0:
        return (y_nodes[1] - y_nodes[0]) / (x_nodes[1] - x_nodes[0])
    if i >= len(x_nodes) - 1:
        return (y_nodes[-1] - y_nodes[-2]) / (x_nodes[-1] - x_nodes[-2])
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
        d_left = derivatives[i - 1]
        d_right = derivatives[i + 1]

        # First derivative test: sign change
        if (d_left > 0 and d_right < 0) or (d_left < 0 and d_right > 0):
            fpp = second_derivatives[i]
            if fpp < 0:
                extrema.append((x_nodes[i], y_nodes[i], "maximum", fpp))
            elif fpp > 0:
                extrema.append((x_nodes[i], y_nodes[i], "minimum", fpp))
            else:
                extrema.append((x_nodes[i], y_nodes[i], "saddle/inconclusive", fpp))

    return extrema, derivatives, second_derivatives


if __name__ == "__main__":
    # Demo: y = (x-3)^2 + 1 — парабола с минимумом при x=3
    x_tab = [1.0, 2.0, 3.0, 4.0, 5.0]
    y_tab = [5.0, 2.0, 1.0, 2.0, 5.0]

    print("--- Analysis of Tabulated Functions ---")
    print("4.1 Maxima and Minima")
    print(f"Data: x = {x_tab}, y = {y_tab}")

    extrema, d1, d2 = find_maxima_minima(x_tab, y_tab)

    print(f"\n4.2 First derivatives (approx): {[round(d, 4) for d in d1]}")
    print(f"4.3 Second derivatives (approx):  {[round(d, 4) for d in d2]}")

    print("\nExtrema found:")
    for x, y, kind, fpp in extrema:
        print(f"  At x = {x}: y = {y} — {kind} (f'' = {fpp:.4f})")
