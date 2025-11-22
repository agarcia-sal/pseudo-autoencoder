from typing import List

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        max_len = len(str(k))  # maximum length of substring to consider

        for i in range(1, n + 1):
            # Only need to look back max_len characters because k limits max length
            for j in range(max(0, i - max_len), i):
                # skip if s[j] == '0' because numbers should not start with zero
                if s[j] == '0':
                    continue

                num = int(s[j:i])
                if 1 <= num <= k:
                    dp[i] = (dp[i] + dp[j]) % MOD
                else:
                    # since numbers are increasing in length, break early if num > k to save time
                    # but only if s[j] != '0', which we already checked
                    # so further expanding substring will only increase num
                    # hence no need to check further j for this i
                    break

        return dp[n]