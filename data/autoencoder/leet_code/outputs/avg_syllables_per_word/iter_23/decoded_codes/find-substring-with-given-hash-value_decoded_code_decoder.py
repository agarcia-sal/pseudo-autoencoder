class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c: str) -> int:
            return ord(c) - ord('a') + 1

        n = len(s)
        current_hash = 0
        p_pow = 1

        # Compute hash of last k characters
        for i in range(n - k, n):
            current_hash = (current_hash + val(s[i]) * p_pow) % modulo
            if i < n - 1:
                p_pow = (p_pow * power) % modulo

        start_index = n - k
        if current_hash == hashValue:
            return s[start_index:]

        p_pow_k_minus_1 = p_pow

        # Rolling hash backward
        for i in range(n - k - 1, -1, -1):
            removed_val = val(s[i + k]) * p_pow_k_minus_1
            current_hash = (current_hash - removed_val) % modulo
            current_hash = (current_hash * power + val(s[i])) % modulo
            if current_hash == hashValue:
                start_index = i

        return s[start_index:start_index + k]