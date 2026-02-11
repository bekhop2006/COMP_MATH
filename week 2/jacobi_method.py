def matrix_copy(A):
    return [row[:] for row in A]

def vector_copy(v):
    return v[:]

def matrix_vector_multiply(A, x):
    n = len(A)
    result = [0.0] * n
    for i in range(n):
        for j in range(len(x)):
            result[i] += A[i][j] * x[j]
    return result

def vector_subtract(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]

def vector_norm(v):
    return sum(x * x for x in v) ** 0.5

def get_diagonal_matrix(A):
    n = len(A)
    D = [[0.0] * n for _ in range(n)]
    for i in range(n):
        D[i][i] = A[i][i]
    return D

def get_lower_triangular(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i):
            L[i][j] = A[i][j]
    return L

def get_upper_triangular(A):
    n = len(A)
    U = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            U[i][j] = A[i][j]
    return U

def matrix_add(A, B):
    n = len(A)
    result = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result

def get_diagonal_inverse(D):
    n = len(D)
    D_inv = [[0.0] * n for _ in range(n)]
    for i in range(n):
        if abs(D[i][i]) < 1e-10:
            raise ValueError("Diagonal element is zero, cannot invert")
        D_inv[i][i] = 1.0 / D[i][i]
    return D_inv

def jacobi_method(A, b, x0=None, tol=1e-6, max_iter=100):
    A = matrix_copy(A)
    b = vector_copy(b)
    n = len(A)
    
    if x0 is None:
        x0 = [0.0] * n
    else:
        x0 = vector_copy(x0)
    
    D = get_diagonal_matrix(A)
    L = get_lower_triangular(A)
    U = get_upper_triangular(A)
    
    D_inv = get_diagonal_inverse(D)
    LU = matrix_add(L, U)
    
    x = vector_copy(x0)
    history = [vector_copy(x)]
    
    for iteration in range(max_iter):
        LUx = matrix_vector_multiply(LU, x)
        b_minus_LUx = vector_subtract(b, LUx)
        x_new = matrix_vector_multiply(D_inv, b_minus_LUx)
        history.append(vector_copy(x_new))
        
        error = vector_norm(vector_subtract(x_new, x))
        if error < tol:
            return x_new, history, iteration + 1
        
        x = x_new
    
    return x, history, max_iter
