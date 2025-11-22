class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = self.convert_list_to_set(wordDict)
        dp = self.initialize_boolean_list(len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[len(s)]

    def convert_list_to_set(self, wordDict):
        return set(wordDict)

    def initialize_boolean_list(self, size):
        return [False] * size