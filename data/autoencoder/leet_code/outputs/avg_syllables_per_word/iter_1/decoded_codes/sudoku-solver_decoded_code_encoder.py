from itertools import product

def is_valid(b, r, c, n):
    return (all(b[r][i] != n for i in range(9)) and
            all(b[i][c] != n for i in range(9)) and
            all(b[3*(r//3)+i][3*(c//3)+j] != n for i, j in product(range(3), range(3))))

def solve(b):
    for r in range(9):
        for c in range(9):
            if b[r][c] == '.':
                for n in '123456789':
                    if is_valid(b, r, c, n):
                        b[r][c] = n
                        if solve(b):
                            return True
                        b[r][c] = '.'
                return False
    return True