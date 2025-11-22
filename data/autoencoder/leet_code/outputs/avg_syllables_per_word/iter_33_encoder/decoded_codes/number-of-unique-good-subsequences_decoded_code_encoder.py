class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7
        end_with_0 = 0
        end_with_1 = 0
        has_zero = 1 if '0' in binary else 0
        for bit in binary:
            if bit == '1':
                end_with_1 = (end_with_0 + end_with_1 + 1) % MOD
            else:
                end_with_0 = (end_with_0 + end_with_1) % MOD
        return (end_with_0 + end_with_1 + has_zero) % MOD