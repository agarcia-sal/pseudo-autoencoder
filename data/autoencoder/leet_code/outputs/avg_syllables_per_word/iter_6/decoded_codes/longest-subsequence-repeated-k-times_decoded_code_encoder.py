from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        valid_chars = [ch for ch in freq if freq[ch] >= k]
        valid_chars.sort(reverse=True)

        def is_valid_subsequence(candidate: str) -> bool:
            count, idx = 0, 0
            for ch in s:
                if ch == candidate[idx]:
                    idx += 1
                    if idx == len(candidate):
                        count += 1
                        idx = 0
                        if count == k:
                            return True
            return False

        best_candidate = ""

        def backtrack(candidate: str):
            nonlocal best_candidate
            if len(candidate) > len(best_candidate):
                best_candidate = candidate
            for ch in valid_chars:
                new_candidate = candidate + ch
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate