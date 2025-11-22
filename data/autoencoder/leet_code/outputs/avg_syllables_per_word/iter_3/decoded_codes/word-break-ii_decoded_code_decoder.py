class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return ['']

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sentence in backtrack(end):
                        if sentence:
                            res.append(word + ' ' + sentence)
                        else:
                            res.append(word)
            memo[start] = res
            return res

        return backtrack(0)