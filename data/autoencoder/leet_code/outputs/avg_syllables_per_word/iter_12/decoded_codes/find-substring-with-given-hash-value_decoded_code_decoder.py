class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c: str) -> int:
            return ord(c) - ord('a') + 1

        n = len(s)
        current_hash = 0
        p_pow = 1

        # Compute hash for the last k characters (reversed order)
        for index in range(n - k, n):
            current_hash = (current_hash + val(s[index]) * p_pow) % modulo
            if index < n - 1:
                p_pow = (p_pow * power) % modulo

        start_index = n - k
        if current_hash == hashValue:
            return s[start_index:]

        p_pow_k_minus_1 = p_pow
        for index in range(n - k - 1, -1, -1):
            current_hash = (current_hash - val(s[index + k]) * p_pow_k_minus_1) % modulo
            current_hash = (current_hash * power + val(s[index])) % modulo
            if current_hash == hashValue:
                start_index = index

        return s[start_index:start_index + k]