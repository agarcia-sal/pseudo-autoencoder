from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        valid_chars = sorted([c for c in freq if freq[c] >= k], reverse=True)
        best_candidate = ""

        def is_valid_subsequence(candidate):
            count = 0
            index = 0
            length = len(candidate)
            for char in s:
                if char == candidate[index]:
                    index += 1
                    if index == length:
                        count += 1
                        if count == k:
                            return True
                        index = 0
            return False

        def backtrack(candidate):
            nonlocal best_candidate
            if len(candidate) > len(best_candidate):
                best_candidate = candidate
            for c in valid_chars:
                new_candidate = candidate + c
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate