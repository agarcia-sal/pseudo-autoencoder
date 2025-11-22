from functools import lru_cache

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MODULO = 10**9 + 7
        total_length = len(num)

        @lru_cache(None)
        def dp(current_index: int, previous_length: int) -> int:
            if current_index == total_length:
                return 1
            if num[current_index] == '0':
                return 0

            count = 0
            for length in range(1, total_length - current_index + 1):
                current_num_str = num[current_index:current_index + length]

                if previous_length == 0:
                    # No previous number to compare, always proceed
                    count += dp(current_index + length, length)
                    count %= MODULO
                else:
                    prev_start = current_index - previous_length
                    prev_end = current_index
                    prev_num_str = num[prev_start:prev_end]

                    # If current_num_str >= prev_num_str lexicographically
                    # but since these are numbers without leading zeros, length comparison first
                    # If lengths differ, longer one is greater,
                    # else lex compare (string compare)
                    if length > previous_length:
                        # current number longer => greater
                        count += dp(current_index + length, length)
                        count %= MODULO
                    elif length == previous_length and current_num_str >= prev_num_str:
                        count += dp(current_index + length, length)
                        count %= MODULO
                    # else current_num_str < prev_num_str, skip

            return count % MODULO

        return dp(0, 0)