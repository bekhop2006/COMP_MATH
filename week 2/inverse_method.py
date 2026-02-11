def matrix_copy(A):
    return [row[:] for row in A]

def matrix_identity(n):
    I = []
    for i in range(n):
        row = [0.0] * n
        row[i] = 1.0
        I.append(row)
    return I

def matrix_vector_multiply(A, x):
    n = len(A)
    result = [0.0] * n
    for i in range(n):
        for j in range(len(x)):
            result[i] += A[i][j] * x[j]
    return result

def matrix_inverse(A):
    A = matrix_copy(A)
    n = len(A)
    
    if n == 0 or len(A[0]) != n:
        raise ValueError("Matrix must be square")
    
    I = matrix_identity(n)
    
    augmented = []
    for i in range(n):
        row = A[i][:] + I[i][:]
        augmented.append(row)
    
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented[k][i]) > abs(augmented[max_row][i]):
                max_row = k
        
        augmented[i], augmented[max_row] = augmented[max_row], augmented[i]
        
        if abs(augmented[i][i]) < 1e-10:
            raise ValueError("Matrix is singular. Inverse matrix does not exist.")
        
        pivot = augmented[i][i]
        for j in range(2 * n):
            augmented[i][j] /= pivot
        
        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]
    
    A_inv = []
    for i in range(n):
        row = augmented[i][n:]
        A_inv.append(row)
    
    return A_inv

def inverse_method(A, b):
    A_inv = matrix_inverse(A)
    x = matrix_vector_multiply(A_inv, b)
    return x
