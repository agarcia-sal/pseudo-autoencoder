def leading_zero(x):
    return len(x) > 1 and x[0] == '0'

def valid_sequence(num, n, start, f, s):
    if start == n:
        return True
    t = str(f + s)
    if num[start:start+len(t)] != t:
        return False
    return valid_sequence(num, n, start + len(t), s, int(t))

def check_sequence(num):
    n = len(num)
    for i in range(1, n // 2 + 1):
        for j in range(i + 1, n + 1):
            first, second = num[:i], num[i:j]
            if leading_zero(first) or leading_zero(second):
                continue
            if valid_sequence(num, n, j, int(first), int(second)):
                return True
    return False