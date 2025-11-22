class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        memo = {}

        def dp(index: int, prev_len: int) -> int:
            if index == n:
                return 1
            if (index, prev_len) in memo:
                return memo[(index, prev_len)]
            count = 0
            max_len = n - index  # maximum length possible from index
            for length in range(1, max_len + 1):
                if num[index] == '0':  # leading zero invalid number
                    break
                current_num = num[index:index + length]
                if prev_len == 0:
                    # no previous number to compare
                    count = (count + dp(index + length, length)) % MOD
                else:
                    prev_num = num[index - prev_len:index]
                    # compare strings based on length and lex order
                    # if lengths are different, longer is larger
                    if length > prev_len:
                        count = (count + dp(index + length, length)) % MOD
                    elif length == prev_len and current_num >= prev_num:
                        count = (count + dp(index + length, length)) % MOD
                    # if length < prev_len, cannot be >= prev_num since shorter
                    # so no addition
            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)