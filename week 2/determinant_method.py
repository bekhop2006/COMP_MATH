def matrix_copy(A):
    return [row[:] for row in A]

def get_minor(A, row, col):
    n = len(A)
    minor = []
    for i in range(n):
        if i != row:
            minor_row = []
            for j in range(n):
                if j != col:
                    minor_row.append(A[i][j])
            minor.append(minor_row)
    return minor

def determinant_gauss(A):
    A = matrix_copy(A)
    n = len(A)
    if n == 0 or len(A[0]) != n:
        raise ValueError("Matrix must be square")
    
    det = 1.0
    sign = 1
    
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            sign *= -1
        
        if abs(A[i][i]) < 1e-10:
            return 0.0
        
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
    
    for i in range(n):
        det *= A[i][i]
    
    return sign * det

def determinant_recursive(A):
    n = len(A)
    if n == 0 or len(A[0]) != n:
        raise ValueError("Matrix must be square")
    
    if n == 1:
        return float(A[0][0])
    
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
    det = 0.0
    for j in range(n):
        minor = get_minor(A, 0, j)
        cofactor = (-1) ** j * A[0][j] * determinant_recursive(minor)
        det += cofactor
    
    return det

def determinant(A, method='gauss'):
    if method == 'gauss':
        return determinant_gauss(A)
    elif method == 'recursive':
        return determinant_recursive(A)
    else:
        raise ValueError("Method must be 'gauss' or 'recursive'")
