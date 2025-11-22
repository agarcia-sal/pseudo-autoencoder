def my_atoi(s: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    res = 0
    i = 0
    n = len(s)
    sign = 1

    while i < n and s[i] == ' ':
        i += 1

    if i < n and s[i] in ['+', '-']:
        sign = -1 if s[i] == '-' else 1
        i += 1

    while i < n and s[i].isdigit():
        d = int(s[i])
        if res > (INT_MAX - d) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        res = res * 10 + d
        i += 1

    return sign * res