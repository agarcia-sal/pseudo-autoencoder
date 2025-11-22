from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        valid_chars = [char for char, count in freq.items() if count >= k]
        valid_chars.sort(reverse=True)

        def is_valid_subsequence(candidate: str) -> bool:
            count = 0
            index = 0
            for char in s:
                if char == candidate[index]:
                    index += 1
                    if index == len(candidate):
                        count += 1
                        index = 0
                        if count == k:
                            return True
            return False

        best_candidate = ""

        def backtrack(candidate: str) -> None:
            nonlocal best_candidate
            if len(candidate) > len(best_candidate):
                best_candidate = candidate
            for char in valid_chars:
                new_candidate = candidate + char
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate