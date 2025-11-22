def sum_prime_factors(n):
    if n == 1:
        return 0
    ops = 0
    f = 2
    while n > 1:
        while n % f == 0:
            ops += f
            n //= f
        f += 1
    return ops