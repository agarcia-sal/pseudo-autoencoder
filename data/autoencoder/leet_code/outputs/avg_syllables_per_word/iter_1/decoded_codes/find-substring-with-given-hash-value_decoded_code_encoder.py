def subStrHash(s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
    def val(c):
        return ord(c) - ord('a') + 1

    n = len(s)
    current_hash = 0
    # Compute initial hash for the last substring of length k
    for i in range(n - k, n):
        current_hash = (current_hash * power + val(s[i])) % modulo

    p_pow_k_1 = pow(power, k - 1, modulo)
    start = n - k if current_hash == hashValue else -1

    for i in range(n - k - 1, -1, -1):
        current_hash = (current_hash - val(s[i + k]) * p_pow_k_1) % modulo
        current_hash = (current_hash * power + val(s[i])) % modulo
        if current_hash == hashValue:
            start = i

    return s[start: start + k]