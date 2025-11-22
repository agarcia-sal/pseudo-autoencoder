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
            for length in range(1, n - index + 1):
                if num[index] == '0':
                    break
                current_num = num[index:index+length]

                if prev_len == 0:
                    # no previous number, always valid
                    count += dp(index + length, length)
                    count %= MOD
                else:
                    prev_start = index - prev_len
                    prev_end = index
                    prev_num = num[prev_start:prev_end]
                    # only continue if current_num >= prev_num in lex order
                    if len(current_num) > len(prev_num):
                        # if current number length longer, it's definitely greater (no leading zeros)
                        count += dp(index + length, length)
                        count %= MOD
                    elif len(current_num) == len(prev_num) and current_num >= prev_num:
                        count += dp(index + length, length)
                        count %= MOD

            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)