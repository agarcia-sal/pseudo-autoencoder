from collections import defaultdict

class Solution:
    def findNumOfValidWords(self, words, puzzles):
        def to_mask(s):
            mask = 0
            for char in s:
                mask |= 1 << (ord(char) - ord('a'))
            return mask

        word_count = defaultdict(int)
        for word in words:
            mask = to_mask(word)
            if bin(mask).count('1') <= 7:
                word_count[mask] += 1

        result = []
        for puzzle in puzzles:
            first_char_mask = 1 << (ord(puzzle[0]) - ord('a'))
            puzzle_mask = to_mask(puzzle[1:])
            count = word_count.get(first_char_mask, 0)

            subset = puzzle_mask
            while subset:
                count += word_count.get(subset | first_char_mask, 0)
                subset = (subset - 1) & puzzle_mask

            result.append(count)

        return result