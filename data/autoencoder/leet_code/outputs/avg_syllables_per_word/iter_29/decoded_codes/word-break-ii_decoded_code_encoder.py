from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def backtrack(start_index: int) -> List[str]:
            if start_index in memo:
                return memo[start_index]

            if start_index == len(s):
                return [""]

            res = []
            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]
                if word in wordSet:
                    for sentence in backtrack(end_index):
                        if sentence:
                            res.append(word + " " + sentence)
                        else:
                            res.append(word)
            memo[start_index] = res
            return res

        return backtrack(0)