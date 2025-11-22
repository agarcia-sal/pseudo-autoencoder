from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)

        valid_chars = [ch for ch, cnt in freq.items() if cnt >= k]
        valid_chars.sort(reverse=True)  # descending lex order

        def is_valid_subsequence(candidate: str) -> bool:
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

        max_len = len(valid_chars) // k
        best_candidate = ""

        def backtrack(candidate: str):
            nonlocal best_candidate
            if len(candidate) > len(best_candidate):
                best_candidate = candidate
            for ch in valid_chars:
                new_candidate = candidate + ch
                # Prune if new_candidate is not a valid subsequence repeated k times
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate