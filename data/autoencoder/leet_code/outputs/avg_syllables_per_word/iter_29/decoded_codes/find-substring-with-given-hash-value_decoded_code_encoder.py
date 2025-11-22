class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(character: str) -> int:
            return ord(character) - ord('a') + 1

        length_of_s = len(s)
        current_hash = 0
        power_to_zero = 1

        # Compute hash for the last k chars of s
        for index in range(length_of_s - k, length_of_s):
            current_hash = (current_hash + val(s[index]) * power_to_zero) % modulo
            if index < length_of_s - 1:
                power_to_zero = (power_to_zero * power) % modulo

        start_index = length_of_s - k
        if current_hash == hashValue:
            return s[start_index:start_index + k]

        power_to_k_minus_one = power_to_zero
        # Roll hash backwards through string s
        for index in range(length_of_s - k - 1, -1, -1):
            removed_char_val = val(s[index + k])
            added_char_val = val(s[index])
            current_hash = (current_hash - removed_char_val * power_to_k_minus_one) % modulo
            current_hash = (current_hash * power + added_char_val) % modulo
            if current_hash == hashValue:
                start_index = index

        return s[start_index:start_index + k]