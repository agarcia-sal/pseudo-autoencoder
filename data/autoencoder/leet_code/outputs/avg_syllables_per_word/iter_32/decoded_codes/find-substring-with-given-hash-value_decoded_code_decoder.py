class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c: str) -> int:
            # map character c to a number as specified
            return ord(c) - ord('a') + 1

        n = len(s)
        current_hash = 0
        p_pow = 1

        # Compute hash for last k characters of s
        for i in range(n - k, n):
            current_hash = (current_hash + val(s[i]) * p_pow) % modulo
            if i < n - 1:
                p_pow = (p_pow * power) % modulo

        start_index = n - k
        if current_hash == hashValue:
            return s[start_index:start_index + k]

        p_pow_k_minus_1 = p_pow  # power^(k-1) modulo

        # Slide over s from right to left
        for i in range(n - k - 1, -1, -1):
            # Remove the character going out of the window, multiply by power^(k-1)
            out_char_val = val(s[i + k]) * p_pow_k_minus_1
            current_hash = (current_hash - out_char_val) % modulo
            # Multiply current_hash by power and add the new character val
            current_hash = (current_hash * power) % modulo
            current_hash = (current_hash + val(s[i])) % modulo

            if current_hash == hashValue:
                start_index = i

        return s[start_index:start_index + k]