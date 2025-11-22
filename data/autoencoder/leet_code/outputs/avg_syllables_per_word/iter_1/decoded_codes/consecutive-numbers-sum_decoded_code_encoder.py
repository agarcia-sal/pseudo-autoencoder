def count_representations(n):
    count = 0
    for k in range(1, n+1):
        if (2 * n) % k == 0:
            m = ((2 * n / k) - k + 1) / 2
            if m > 0 and m.is_integer():
                count += 1
    return count