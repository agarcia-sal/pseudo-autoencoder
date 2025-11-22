from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, input_string: str, repetition_count: int) -> str:
        frequency_map = Counter(input_string)
        valid_characters = [ch for ch, count in frequency_map.items() if count >= repetition_count]
        valid_characters.sort(reverse=True)  # descending lex order

        # Verify if candidate_subsequence repeated repetition_count times is a subsequence of input_string
        def is_valid_subsequence(candidate_subsequence: str) -> bool:
            occurrence_count = 0
            position_index = 0
            length = len(candidate_subsequence)
            for ch in input_string:
                if ch == candidate_subsequence[position_index]:
                    position_index += 1
                    if position_index == length:
                        occurrence_count += 1
                        if occurrence_count == repetition_count:
                            return True
                        position_index = 0
            return False

        best_candidate = ""

        def backtrack(current_candidate: str):
            nonlocal best_candidate
            if len(current_candidate) > len(best_candidate):
                best_candidate = current_candidate
            for ch in valid_characters:
                new_candidate = current_candidate + ch
                if is_valid_subsequence(new_candidate):
                    backtrack(new_candidate)

        backtrack("")
        return best_candidate