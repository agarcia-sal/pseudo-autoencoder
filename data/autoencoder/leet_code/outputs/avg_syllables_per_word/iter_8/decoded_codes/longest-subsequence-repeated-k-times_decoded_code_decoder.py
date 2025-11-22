from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s, k):
        def is_valid_subsequence(candidate):
            count = 0
            index = 0
            length = len(candidate)
            for char in s:
                if char == candidate[index]:
                    index += 1
                    if index == length:
                        count += 1
                        index = 0
                        if count == k:
                            return True
            return False

        freq = Counter(s)
        valid_chars = [c for c in freq if freq[c] >= k]
        valid_chars.sort(reverse=True)

        best_candidate = ""

        def backtrack(candidate):
            nonlocal best_candidate
            if len(candidate) > len(best_candidate):
                best_candidate = candidate
            for char in valid_chars:
                new_candidate = candidate + char
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate