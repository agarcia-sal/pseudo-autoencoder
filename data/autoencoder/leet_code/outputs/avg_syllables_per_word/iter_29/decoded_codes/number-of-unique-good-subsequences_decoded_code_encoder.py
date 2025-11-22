class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MODULO = 10**9 + 7
        count_of_subsequences_ending_with_zero = 0
        count_of_subsequences_ending_with_one = 0
        contains_zero = 1 if '0' in binary else 0

        for bit in binary:
            if bit == '1':
                count_of_subsequences_ending_with_one = (count_of_subsequences_ending_with_zero + count_of_subsequences_ending_with_one + 1) % MODULO
            else:
                count_of_subsequences_ending_with_zero = (count_of_subsequences_ending_with_zero + count_of_subsequences_ending_with_one) % MODULO

        total_unique_good_subsequences = (count_of_subsequences_ending_with_zero + count_of_subsequences_ending_with_one + contains_zero) % MODULO
        return total_unique_good_subsequences