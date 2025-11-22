class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MODULO = 10**9 + 7
        countSubsequencesEndingWithZero = 0
        countSubsequencesEndingWithOne = 0
        containsZero = 1 if '0' in binary else 0
        for bit in binary:
            if bit == '1':
                countSubsequencesEndingWithOne = (countSubsequencesEndingWithZero + countSubsequencesEndingWithOne + 1) % MODULO
            else:
                countSubsequencesEndingWithZero = (countSubsequencesEndingWithZero + countSubsequencesEndingWithOne) % MODULO
        totalUniqueGoodSubsequences = (countSubsequencesEndingWithZero + countSubsequencesEndingWithOne + containsZero) % MODULO
        return totalUniqueGoodSubsequences