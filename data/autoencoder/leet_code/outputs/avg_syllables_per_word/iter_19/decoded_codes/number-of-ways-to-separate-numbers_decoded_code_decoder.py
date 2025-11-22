class Solution:
    def numberOfCombinations(self, num):
        MOD = 10**9 + 7
        n = len(num)
        memo = {}

        def dp(index, prev_len):
            if index == n:
                return 1
            if (index, prev_len) in memo:
                return memo[(index, prev_len)]

            count = 0
            # If the current character is '0', no valid number can start here
            if num[index] == '0':
                memo[(index, prev_len)] = 0
                return 0

            for length in range(1, n - index + 1):
                # If prev_len == 0, there is no previous number, so any number is allowed
                if prev_len == 0:
                    count += dp(index + length, length)
                    count %= MOD
                else:
                    # Compare current number with previous number of length prev_len
                    prev_start = index - prev_len
                    # If prev_start < 0, then no previous number, treat as allowed
                    if prev_start < 0:
                        count += dp(index + length, length)
                        count %= MOD
                    else:
                        prev_num = num[prev_start:prev_start + prev_len]
                        # current_num is num[index:index+length]
                        # Compare lex order to ensure current_num >= prev_num
                        # Only if lengths are equal, lex order directly; if lengths differ, longer number is greater
                        if length > prev_len:
                            count += dp(index + length, length)
                            count %= MOD
                        elif length == prev_len and num[index:index + length] >= prev_num:
                            count += dp(index + length, length)
                            count %= MOD
                        # if length < prev_len, current_num is definitely smaller
                        # so not valid, do nothing

            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)