class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MODULO = 10**9 + 7
        end_with_zero = 0
        end_with_one = 0
        has_zero = 1 if '0' in binary else 0

        for bit in binary:
            if bit == '1':
                end_with_one = (end_with_zero + end_with_one + 1) % MODULO
            else:
                end_with_zero = (end_with_zero + end_with_one) % MODULO

        return (end_with_zero + end_with_one + has_zero) % MODULO