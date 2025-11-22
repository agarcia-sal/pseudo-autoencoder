class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MODULO_VALUE = 10**9 + 7
        count_of_subsequences_ending_with_zero = 0
        count_of_subsequences_ending_with_one = 0
        presence_of_zero = 1 if '0' in binary else 0

        for bit_character in binary:
            if bit_character == '1':
                count_of_subsequences_ending_with_one = (count_of_subsequences_ending_with_zero + count_of_subsequences_ending_with_one + 1) % MODULO_VALUE
            elif bit_character == '0':
                count_of_subsequences_ending_with_zero = (count_of_subsequences_ending_with_zero + count_of_subsequences_ending_with_one) % MODULO_VALUE

        total_unique_good_subsequences = (count_of_subsequences_ending_with_zero + count_of_subsequences_ending_with_one + presence_of_zero) % MODULO_VALUE
        return total_unique_good_subsequences