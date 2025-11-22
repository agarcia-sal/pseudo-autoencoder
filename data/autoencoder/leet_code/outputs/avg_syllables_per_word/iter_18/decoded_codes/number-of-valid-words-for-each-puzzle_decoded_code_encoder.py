from collections import defaultdict
from typing import List

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def to_mask(s: str) -> int:
            mask = 0
            for ch in s:
                mask |= 1 << (ord(ch) - ord('a'))
            return mask

        word_count = defaultdict(int)

        for word in words:
            mask = to_mask(word)
            # Check if the number of unique letters is <= 7
            if bin(mask).count('1') <= 7:
                word_count[mask] += 1

        result = []

        for puzzle in puzzles:
            first_char_mask = 1 << (ord(puzzle[0]) - ord('a'))
            puzzle_mask = to_mask(puzzle[1:])
            count = word_count[first_char_mask]

            subset = puzzle_mask
            while subset:
                combined_mask = subset | first_char_mask
                count += word_count[combined_mask]
                subset = (subset - 1) & puzzle_mask

            result.append(count)

        return result