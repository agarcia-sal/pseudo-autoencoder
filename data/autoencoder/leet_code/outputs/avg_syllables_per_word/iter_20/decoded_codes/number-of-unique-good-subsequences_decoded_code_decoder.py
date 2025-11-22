class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MODULO = 10**9 + 7
        count_of_subsequences_ending_with_zero = 0
        count_of_subsequences_ending_with_one = 0
        binary_contains_zero = int('0' in binary)

        for bit in binary:
            if bit == '1':
                count_of_subsequences_ending_with_one = (
                    count_of_subsequences_ending_with_zero
                    + count_of_subsequences_ending_with_one
                    + 1
                ) % MODULO
            else:
                count_of_subsequences_ending_with_zero = (
                    count_of_subsequences_ending_with_zero
                    + count_of_subsequences_ending_with_one
                ) % MODULO

        return (count_of_subsequences_ending_zero := count_of_subsequences_ending_zero if 'count_of_subsequences_ending_zero' in locals() else 0) + (
            count_of_subsequences_ending_one := count_of_subsequences_ending_one if 'count_of_subsequences_ending_one' in locals() else 0) + binary_contains_zero) % MODULO