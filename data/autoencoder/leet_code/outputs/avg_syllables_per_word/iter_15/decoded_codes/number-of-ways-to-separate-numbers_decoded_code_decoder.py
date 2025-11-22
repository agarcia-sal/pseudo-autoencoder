class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MODULO = 10**9 + 7
        n = len(num)
        memoization_dictionary = {}

        def dp(index: int, previous_length: int) -> int:
            if index == n:
                return 1
            if (index, previous_length) in memoization_dictionary:
                return memoization_dictionary[(index, previous_length)]

            count = 0
            # If num[index] == '0', no valid number can start with zero, break immediately.
            if num[index] == '0':
                memoization_dictionary[(index, previous_length)] = 0
                return 0

            # Explore all possible lengths for the next number starting at index
            for length in range(1, n - index + 1):
                current_number = num[index:index + length]
                # previous_length == 0 means no previous number to compare with
                if previous_length == 0:
                    count = (count + dp(index + length, length)) % MODULO
                else:
                    # Get the previous number substring
                    prev_start = index - previous_length
                    prev_number = num[prev_start: index]
                    # Compare lex order as strings because numbers can be large
                    if length > previous_length or (length == previous_length and current_number >= prev_number):
                        count = (count + dp(index + length, length)) % MODULO
                    else:
                        # Current number smaller than previous, so skip
                        pass

            memoization_dictionary[(index, previous_length)] = count
            return count

        return dp(0, 0)