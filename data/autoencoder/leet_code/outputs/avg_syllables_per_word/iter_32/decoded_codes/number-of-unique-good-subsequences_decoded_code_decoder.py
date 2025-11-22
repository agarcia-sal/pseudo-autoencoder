class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7
        end_with_zero = 0
        end_with_one = 0
        has_zero = 1 if '0' in binary else 0

        for bit in binary:
            if bit == '1':
                end_with_one = (end_with_zero + end_with_one + 1) % MOD
            else:
                end_with_zero = (end_with_zero + end_with_one) % MOD

        return (end_with_zero + end_with_one + has_zero) % MOD