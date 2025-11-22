from collections import defaultdict

class Solution:
    def findNumOfValidWords(self, words, puzzles):
        def to_mask(s):
            mask = 0
            for ch in s:
                shift_amount = ord(ch) - ord('a')
                mask |= 1 << shift_amount
            return mask

        word_count = defaultdict(int)
        for word in words:
            mask = to_mask(word)
            # only count words with up to 7 unique letters
            if bin(mask).count('1') <= 7:
                word_count[mask] += 1

        result = []
        for puzzle in puzzles:
            shift_amount_first = ord(puzzle[0]) - ord('a')
            first_char_mask = 1 << shift_amount_first
            puzzle_mask = to_mask(puzzle[1:])
            count = word_count.get(first_char_mask, 0)

            subset = puzzle_mask
            while subset > 0:
                union_mask = subset | first_char_mask
                count += word_count.get(union_mask, 0)
                subset = (subset - 1) & puzzle_mask

            result.append(count)

        return result