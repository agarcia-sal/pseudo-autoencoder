class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        memo = {}

        def dp(index: int, prev_len: int) -> int:
            if index == n:
                return 1
            key = (index, prev_len)
            if key in memo:
                return memo[key]
            count = 0
            # If num[index] == '0' no valid number starts here
            if num[index] == '0':
                memo[key] = 0
                return 0

            max_len = n - index
            for length in range(1, max_len + 1):
                # If prev_len == 0 means no previous number, so always valid
                if prev_len == 0:
                    count = (count + dp(index + length, length)) % MOD
                else:
                    # Compare current substring with the previous substring of length prev_len
                    if length >= prev_len:
                        prev_start = index - prev_len
                        prev_end = index
                        prev_sub = num[prev_start:prev_end]
                        curr_sub = num[index:index+length]
                        # If lengths differ, the longer substring represents a bigger number
                        if length > prev_len or curr_sub >= prev_sub:
                            count = (count + dp(index + length, length)) % MOD
                    else:
                        # length < prev_len => current number shorter than previous number -> no need to check
                        # because it can't be >= previous number (numerically)
                        pass
                # If num[index] == '0' breaking above covers, so no inner break needed here
            memo[key] = count
            return count

        return dp(0, 0)