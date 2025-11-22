from collections import defaultdict
from typing import List

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def to_mask(s: str) -> int:
            mask = 0
            for ch in s:
                bit_position = ord(ch) - ord('a')
                mask |= 1 << bit_position
            return mask

        word_count = defaultdict(int)

        for word in words:
            mask = to_mask(word)
            # Count only words with up to 7 unique characters
            if bin(mask).count('1') <= 7:
                word_count[mask] += 1

        result = []

        for puzzle in puzzles:
            first_char_bit_position = ord(puzzle[0]) - ord('a')
            first_char_mask = 1 << first_char_bit_position
            puzzle_mask = to_mask(puzzle[1:])
            count = 0

            subset = puzzle_mask
            while subset:
                combined_mask = subset | first_char_mask
                count += word_count.get(combined_mask, 0)
                subset = (subset - 1) & puzzle_mask
            # Include the word_count for only the first_char_mask alone if present
            count += word_count.get(first_char_mask, 0)
            result.append(count)

        return result