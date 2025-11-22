from collections import Counter
from typing import List


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)

        valid_chars: List[str] = []
        for char, count in freq.items():
            if count >= k:
                valid_chars.append(char)

        # Sort descending lex order
        valid_chars.sort(reverse=True)

        def is_valid_subsequence(candidate: str) -> bool:
            count = 0
            index = 0
            cand_len = len(candidate)
            for ch in s:
                if cand_len == 0:
                    break  # empty candidate always valid candidate; just safety
                if ch == candidate[index]:
                    index += 1
                    if index == cand_len:
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