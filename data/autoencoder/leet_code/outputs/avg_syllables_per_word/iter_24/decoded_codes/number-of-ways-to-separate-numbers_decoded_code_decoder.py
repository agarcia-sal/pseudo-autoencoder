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

            if num[index] == '0':
                memo[(index, prev_len)] = 0
                return 0

            count = 0
            max_len = n - index
            for length in range(1, max_len + 1):
                # If prev_len == 0, no previous number to compare to
                if prev_len == 0:
                    count += dp(index + length, length)
                    count %= MOD
                else:
                    prev_start = index - prev_len
                    prev_end = index
                    # The previous number substring
                    prev_num = num[prev_start:prev_end]
                    # The current number substring
                    curr_num = num[index:index + length]

                    # Compare lengths: if current length > prev_len -> current_num > prev_num
                    if length > prev_len:
                        count += dp(index + length, length)
                        count %= MOD
                    elif length < prev_len:
                        # current_num smaller length -> definitely smaller
                        continue
                    else:
                        # length == prev_len, compare lex order
                        if curr_num >= prev_num:
                            count += dp(index + length, length)
                            count %= MOD
                        else:
                            continue
            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)