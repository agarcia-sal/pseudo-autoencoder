from collections import defaultdict
from typing import List

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def to_mask(input_string: str) -> int:
            mask = 0
            for ch in input_string:
                bit_position = ord(ch) - ord('a')
                mask |= 1 << bit_position
            return mask

        word_count = defaultdict(int)
        for word in words:
            mask = to_mask(word)
            # Count bits set in mask; if <= 7, add to count
            if bin(mask).count('1') <= 7:
                word_count[mask] += 1

        result = []
        for puzzle in puzzles:
            first_char_bit_position = ord(puzzle[0]) - ord('a')
            first_char_mask = 1 << first_char_bit_position
            puzzle_mask = to_mask(puzzle[1:])
            count = word_count[first_char_mask]  # words containing only the first char mask

            subset = puzzle_mask
            while subset:
                union_mask = subset | first_char_mask
                count += word_count[union_mask]
                subset = (subset - 1) & puzzle_mask

            result.append(count)

        return result