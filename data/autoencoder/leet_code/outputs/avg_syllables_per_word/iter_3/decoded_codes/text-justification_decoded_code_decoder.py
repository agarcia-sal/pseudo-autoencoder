from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line: List[str], num_of_letters: int, is_last_line: bool) -> str:
            if len(line) == 1 or is_last_line:
                return ' '.join(line) + ' ' * (maxWidth - num_of_letters - (len(line) - 1))
            total_spaces = maxWidth - num_of_letters
            num_of_gaps = len(line) - 1
            spaces_between_words, extra_spaces = divmod(total_spaces, num_of_gaps)
            for i in range(extra_spaces):
                line[i] += ' '
            return ''.join(word + ' ' * spaces_between_words for word in line)

        result = []
        line = []
        num_of_letters = 0

        for word in words:
            if num_of_letters + len(word) + len(line) > maxWidth:
                result.append(justify_line(line, num_of_letters, False))
                line = []
                num_of_letters = 0
            line.append(word)
            num_of_letters += len(word)
        result.append(justify_line(line, num_of_letters, True))

        return result