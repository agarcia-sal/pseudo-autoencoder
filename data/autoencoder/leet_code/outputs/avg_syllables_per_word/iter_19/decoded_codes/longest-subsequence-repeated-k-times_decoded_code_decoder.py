from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s, k):
        freq = Counter(s)
        valid_chars = [ch for ch in freq if freq[ch] >= k]
        valid_chars.sort(reverse=True)

        best_candidate = ""

        def is_valid_subsequence(candidate):
            count = 0
            index = 0
            length = len(candidate)
            for ch in s:
                if ch == candidate[index]:
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
            for ch in valid_chars:
                new_candidate = candidate + ch
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate