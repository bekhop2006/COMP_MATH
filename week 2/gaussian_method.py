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

def gaussian_elimination(A, b):
    A = matrix_copy(A)
    b = vector_copy(b)
    n = len(A)
    
    Ab = []
    for i in range(n):
        row = A[i][:] + [b[i]]
        Ab.append(row)
    
    history = [matrix_copy(Ab)]
    
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(Ab[k][i]) > abs(Ab[max_row][i]):
                max_row = k
        
        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]
        history.append(matrix_copy(Ab))
        
        if abs(Ab[i][i]) < 1e-10:
            raise ValueError("Matrix is singular or close to singular")
        
        for k in range(i + 1, n):
            factor = Ab[k][i] / Ab[i][i]
            for j in range(i, n + 1):
                Ab[k][j] -= factor * Ab[i][j]
        history.append(matrix_copy(Ab))
    
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i][n]
        for j in range(i + 1, n):
            x[i] -= Ab[i][j] * x[j]
        x[i] /= Ab[i][i]
    
    return x, history
