def is_sorted_str_of_power_of_two(n):
    P = set()
    p = 1
    while p <= 10**9:
        P.add(''.join(sorted(str(p))))
        p *= 2
    return ''.join(sorted(str(n))) in P