class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MODULO = 10**9 + 1
        n = len(num)
        memo = {}

        def dp(index: int, previous_length: int) -> int:
            if index == n:
                return 1
            if (index, previous_length) in memo:
                return memo[(index, previous_length)]

            count = 0
            end_limit = n - index
            for length in range(1, end_limit + 1):
                if num[index] == '0':
                    break
                current_number = num[index:index+length]
                if previous_length == 0 or current_number >= num[index - previous_length:index]:
                    count = (count + dp(index + length, length)) % MODULO

            memo[(index, previous_length)] = count
            return count

        return dp(0, 0)