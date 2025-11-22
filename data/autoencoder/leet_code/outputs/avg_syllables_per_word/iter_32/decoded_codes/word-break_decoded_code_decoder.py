from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                # If s[:j] can be segmented and s[j:i] is a word, mark dp[i] True
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]