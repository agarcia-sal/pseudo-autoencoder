from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        frequency_map = Counter(s)
        valid_chars = [ch for ch in frequency_map if frequency_map[ch] >= k]
        valid_chars.sort(reverse=True)

        best_candidate = ""

        def is_valid_subsequence(candidate: str) -> bool:
            count = 0
            index = 0
            length = len(candidate)
            for ch in s:
                if ch == candidate[index]:
                    index += 1
                    if index == length:
                        count += 1
                        index = 0
                        if count == k:
                            return True
            return False

        def backtrack(candidate: str) -> None:
            nonlocal best_candidate
            if len(candidate) > len(best_candidate):
                best_candidate = candidate
            for ch in valid_chars:
                new_candidate = candidate + ch
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate