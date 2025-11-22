from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        frequency_map = Counter(s)
        valid_characters = [ch for ch, cnt in frequency_map.items() if cnt >= k]
        valid_characters.sort(reverse=True)

        best_candidate = ""

        def is_valid_subsequence(candidate: str) -> bool:
            occurrence_count = 0
            candidate_index = 0
            length = len(candidate)
            for ch in s:
                if candidate_index < length and ch == candidate[candidate_index]:
                    candidate_index += 1
                    if candidate_index == length:
                        occurrence_count += 1
                        candidate_index = 0
                        if occurrence_count == k:
                            return True
            return False

        def backtrack(candidate: str):
            nonlocal best_candidate
            if len(candidate) > len(best_candidate):
                best_candidate = candidate
            for ch in valid_characters:
                new_candidate = candidate + ch
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate