class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                # substring s[j:i], inclusive of j and exclusive of i
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(s)]