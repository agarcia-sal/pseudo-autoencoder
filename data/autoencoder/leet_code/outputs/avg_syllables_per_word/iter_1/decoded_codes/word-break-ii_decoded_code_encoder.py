def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    memo = {}

    def backtrack(start):
        if start in memo:
            return memo[start]
        if start == len(s):
            return [""]

        res = []
        for end in range(start + 1, len(s) + 1):
            w = s[start:end]
            if w in wordSet:
                for sent in backtrack(end):
                    res.append(w + (" " + sent if sent else ""))
        memo[start] = res
        return res

    return backtrack(0)