from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        valid_chars = [ch for ch, count in freq.items() if count >= k]
        valid_chars.sort(reverse=True)  # descending lex order

        def is_valid_subsequence(candidate: str) -> bool:
            count = 0
            index = 0
            for ch in s:
                if ch == candidate[index]:
                    index += 1
                    if index == len(candidate):
                        count += 1
                        if count == k:
                            return True
                        index = 0
            return False

        best_candidate = ""

        def backtrack(candidate: str) -> None:
            nonlocal best_candidate
            if len(candidate) > len(best_candidate):
                best_candidate = candidate
            for ch in valid_chars:
                new_candidate = candidate + ch
                # Only recurse if candidate is possible to repeat k times as subsequence
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate