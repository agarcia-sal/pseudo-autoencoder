from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def is_valid_subsequence(candidate: str) -> bool:
            count = 0
            index = 0
            for ch in s:
                if ch == candidate[index]:
                    index += 1
                    if index == len(candidate):
                        count += 1
                        index = 0
                        if count == k:
                            return True
            return False

        frequency_map = Counter(s)
        valid_characters = [ch for ch, cnt in frequency_map.items() if cnt >= k]
        valid_characters.sort(reverse=True)

        best_candidate = ""

        def backtrack(candidate: str) -> None:
            nonlocal best_candidate
            if len(candidate) > len(best_candidate):
                best_candidate = candidate
            for ch in valid_characters:
                new_candidate = candidate + ch
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate