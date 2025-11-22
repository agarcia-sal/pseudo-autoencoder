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
            # Count words with at most 7 unique letters
            # Only if number of set bits <= 7
            if bin(mask).count('1') <= 7:
                word_count[mask] += 1

        result = []
        for puzzle in puzzles:
            first_char_mask = 1 << (ord(puzzle[0]) - ord('a'))
            # Mask for characters from the second character onward
            puzzle_mask = to_mask(puzzle[1:])
            count = word_count.get(first_char_mask, 0)

            subset = puzzle_mask
            while subset:
                combined_mask = subset | first_char_mask
                count += word_count.get(combined_mask, 0)
                subset = (subset - 1) & puzzle_mask

            result.append(count)

        return result