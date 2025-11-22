def matrix_multiply(mat1, mat2):
    m, k = len(mat1), len(mat1[0])
    k2, n = len(mat2), len(mat2[0])
    if k != k2:
        raise ValueError("mat1 columns must equal mat2 rows")
    result = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for p in range(k):
                result[i][j] += mat1[i][p] * mat2[p][j]
    return result