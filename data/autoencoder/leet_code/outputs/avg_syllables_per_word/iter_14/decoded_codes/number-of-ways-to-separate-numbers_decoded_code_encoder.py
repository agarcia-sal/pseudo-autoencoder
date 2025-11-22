class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MODULO_VALUE = 10**9 + 7
        string_length = len(num)
        memo = {}

        def dp(index: int, previous_length: int) -> int:
            if index == string_length:
                return 1

            key = (index, previous_length)
            if key in memo:
                return memo[key]

            count = 0
            for length in range(1, string_length - index + 1):
                if num[index] == '0':
                    break

                current_number_string = num[index:index + length]

                if previous_length == 0:
                    valid = True
                else:
                    prev_number_string = num[index - previous_length:index]
                    # As strings, lex comparison works correctly for equal length
                    # But need to ensure correct numeric comparison, so:
                    if len(current_number_string) == len(prev_number_string):
                        valid = current_number_string >= prev_number_string
                    else:
                        # If lengths differ, the longer number is larger
                        valid = len(current_number_string) > len(prev_number_string)

                if valid:
                    count += dp(index + length, length)
                    count %= MODULO_VALUE

            memo[key] = count
            return count

        return dp(0, 0)