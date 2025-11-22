class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 1
        n = len(num)
        memo = {}

        def dp(index: int, prev_len: int) -> int:
            if index == n:
                return 1
            if (index, prev_len) in memo:
                return memo[(index, prev_len)]

            if num[index] == '0':  # Leading zero numbers are invalid
                memo[(index, prev_len)] = 0
                return 0

            count = 0
            max_len = n - index
            for length in range(1, max_len + 1):
                current_num = num[index:index + length]

                if prev_len == 0:
                    valid = True
                else:
                    prev_num = num[index - prev_len:index]
                    # Compare as strings of equal length or unequal length by length first
                    if len(current_num) > len(prev_num):
                        valid = True
                    elif len(current_num) < len(prev_num):
                        valid = False
                    else:
                        valid = current_num >= prev_num

                if not valid:
                    continue

                count = (count + dp(index + length, length)) % MOD

            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)