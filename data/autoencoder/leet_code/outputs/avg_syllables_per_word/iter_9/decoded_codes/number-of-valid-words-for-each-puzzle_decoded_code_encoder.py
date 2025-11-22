from collections import Counter

class Solution:
    def findNumOfValidWords(self, words, puzzles):
        def to_mask(s):
            mask = 0
            for ch in s:
                mask |= 1 << (ord(ch) - ord('a'))
            return mask

        word_count = Counter()
        for word in words:
            mask = to_mask(word)
            if bin(mask).count('1') <= 7:
                word_count[mask] += 1

        result = []
        for puzzle in puzzles:
            first_char_mask = 1 << (ord(puzzle[0]) - ord('a'))
            puzzle_mask = to_mask(puzzle[1:])
            count = word_count[first_char_mask]

            subset = puzzle_mask
            while subset:
                count += word_count[subset | first_char_mask]
                subset = (subset - 1) & puzzle_mask

            result.append(count)

        return result