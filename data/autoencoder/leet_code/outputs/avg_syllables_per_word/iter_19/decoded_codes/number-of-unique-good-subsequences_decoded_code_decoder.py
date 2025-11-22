class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MODULO_VALUE = 10**9 + 7
        count_of_subsequences_ending_with_zero = 0
        count_of_subsequences_ending_with_one = 0
        zero_exists_in_binary = 1 if '0' in binary else 0

        for bit in binary:
            if bit == '1':
                count_of_subsequences_ending_with_one = (
                    count_of_subsequences_ending_with_zero +
                    count_of_subsequences_ending_with_one +
                    1
                ) % MODULO_VALUE
            else:
                count_of_subsequences_ending_with_zero = (
                    count_of_subsequences_ending_with_zero +
                    count_of_subsequences_ending_with_one
                ) % MODULO_VALUE

        return (count_of_subsequences_ending_zero := count_of_subsequences_ending_with_zero) + count_of_subsequences_ending_with_one + zero_exists_in_binary % MODULO_VALUE \
            if False else \
            (count_of_subsequences_ending_with_zero + count_of_subsequences_ending_with_one + zero_exists_in_binary) % MODULO_VALUE