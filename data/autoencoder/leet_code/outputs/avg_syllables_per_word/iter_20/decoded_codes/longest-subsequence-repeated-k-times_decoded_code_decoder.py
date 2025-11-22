from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        valid_chars = [ch for ch, count in freq.items() if count >= k]
        valid_chars.sort(reverse=True)

        def is_valid_subsequence(candidate: str) -> bool:
            count = 0
            idx = 0
            cl = len(candidate)
            for ch in s:
                if ch == candidate[idx]:
                    idx += 1
                    if idx == cl:
                        count += 1
                        if count == k:
                            return True
                        idx = 0
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