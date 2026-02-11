import copy

matrix_A = [
    [10.0, -7.0, 3.0, 5.0],
    [-6.0, 8.0, -1.0, -4.0],
    [3.0, 1.0, 4.0, 11.0],
    [5.0 ,-9.0,-2.0, 4.0]
]
vector_B = [6.0, 5.0, 2.0, 7.0]

n = len(matrix_A)


def print_matrix(M):
    for row in M:
        print(["{:.4f}".format(x) for x in row])


# 1. НАХОЖДЕНИЕ ДЕТЕРМИНАНТА (Рекурсивный метод)
# Вычисляет определитель квадратной матрицы рекурсивно через разложение по первой строке.

def get_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0] # det = a

    #  det = a×d - b×c
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # det = a×d - b×c + c×f - d×e + e×b - f×a
    det = 0
    for c in range(len(matrix)):
        sub_matrix = []
        for r in range(1, len(matrix)):
            sub_row = matrix[r][:c] + matrix[r][c + 1:]
            sub_matrix.append(sub_row)

        sign = (-1) ** (c % 2) 
        sub_det = get_determinant(sub_matrix)  # Рекурсивный вызов
        det += sign * matrix[0][c] * sub_det

    return det


print("\n--- 1. DETERMINANT ---")
det_A = get_determinant(matrix_A)
print(f"Determinant = {det_A}")


# 2. ОБРАТНАЯ МАТРИЦА (Метод Гаусса-Жордана с присоединенной матрицей)
# Вычисляет обратную матрицу A⁻¹ методом Гаусса-Жордана.

def get_inverse(matrix):
    n = len(matrix)
    aug_matrix = copy.deepcopy(matrix)
# create augmented matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                aug_matrix[i].append(1.00)
            else:
                aug_matrix[i].append(0.0)
# Гауссовское исключение
    for i in range(n):
        pivot = aug_matrix[i][i]
        if abs(pivot) < 1e-10:
            raise ZeroDivisionError("Matrix is singular, inverse does not exist.")
        # делим на pivot
        for j in range(2 * n):
            aug_matrix[i][j] /= pivot
# обнуляем столбец i, кроме i-го элемента
        for k in range(n):
            if k != i:
                factor = aug_matrix[k][i]
                for j in range(2 * n):
                    aug_matrix[k][j] -= factor * aug_matrix[i][j]

    inverse_mat = []
    for i in range(n):
        inverse_mat.append(aug_matrix[i][n:])

    return inverse_mat


print("\n--- 2. INVERSE MATRIX ---")
try:
    inv_A = get_inverse(matrix_A)
    print("Inverse Matrix:")
    print_matrix(inv_A)
except ZeroDivisionError:
    print("Matrix is singular, inverse does not exist.")


# 3. ДАЙРЕКТ МЕТОД: Метод Гаусса (Gaussian Elimination)
# Решает систему линейных уравнений Ax = b прямым методом.

def solve_gaussian(A_in, b_in):
    A = copy.deepcopy(A_in)
    b = copy.deepcopy(b_in)
    n = len(A)

    # Гауссовское исключение
    for i in range(n):
        pivot = A[i][i]
        if abs(pivot) < 1e-10:
            raise ValueError("Matrix is singular or close to singular")
        # делим на pivot
        for j in range(i, n):
            A[i][j] /= pivot
        b[i] /= pivot
        # обнуляем столбец i, кроме i-го элемента
        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            b[k] -= factor * b[i]
    # обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += A[i][j] * x[j]
        x[i] = b[i] - sum_ax

    return x

print("\n--- 3. DIRECT METHOD (Gaussian) ---")
solution_direct = solve_gaussian(matrix_A, vector_B)
print(f"Solution: {[round(val, 4) for val in solution_direct]}")


# 4. ИТЕРАЦИОННЫЙ МЕТОД: Гаусс-Зейдель (Gauss-Seidel)
# Решает Ax = b итеративно, используя обновленные значения сразу.

def solve_gauss_seidel(A, b, tolerance=0.0001, max_iterations=100):
    n = len(A)
    x = [0.0] * n

    print(f"Iter 0: {x}")
    # итерации
    for k in range(max_iterations):
        x_old = list(x)
        # итерация i
        for i in range(n):
            if abs(A[i][i]) < 1e-10:
                raise ValueError("Diagonal element is zero, cannot solve with Gauss-Seidel")
            
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]

            x[i] = (b[i] - sigma) / A[i][i]

        error = sum([abs(x[i] - x_old[i]) for i in range(n)])
        print(f"Iter {k + 1}: {[round(val, 4) for val in x]}, Error: {round(error, 5)}")

        if error < tolerance:
            print("Converged!")
            return x


    return x


print("\n--- 4. ITERATIVE METHOD (Gauss-Seidel) ---")
solution_iterative = solve_gauss_seidel(matrix_A, vector_B)
print(f"Final Solution: {[round(val, 4) for val in solution_iterative]}")
