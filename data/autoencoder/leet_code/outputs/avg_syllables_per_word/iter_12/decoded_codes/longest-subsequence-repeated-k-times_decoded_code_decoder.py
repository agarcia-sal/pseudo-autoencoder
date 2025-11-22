from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)

        valid_chars = [char for char, count in freq.items() if count >= k]
        valid_chars.sort(reverse=True)

        best_candidate = ""

        def is_valid_subsequence(candidate: str) -> bool:
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

        def backtrack(candidate: str):
            nonlocal best_candidate
            if len(candidate) > len(best_candidate):
                best_candidate = candidate
            for char in valid_chars:
                new_candidate = candidate + char
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate