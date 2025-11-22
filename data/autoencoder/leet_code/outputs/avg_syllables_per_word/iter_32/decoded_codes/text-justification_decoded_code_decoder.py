from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line: List[str], num_of_letters: int, is_last_line: bool) -> str:
            if len(line) == 1 or is_last_line:
                # Left justify: words separated by single spaces, then pad with spaces to maxWidth
                line_str = ' '.join(line)
                return line_str + ' ' * (maxWidth - len(line_str))

            total_spaces = maxWidth - num_of_letters
            num_of_gaps = len(line) - 1
            spaces_between_words, extra_spaces = divmod(total_spaces, num_of_gaps)

            for i in range(num_of_gaps):
                # Append spaces to line[i]
                if i < extra_spaces:
                    line[i] += ' ' * (spaces_between_words + 1)
                else:
                    line[i] += ' ' * spaces_between_words

            return ''.join(line)

        result = []
        line = []
        num_of_letters = 0

        for word in words:
            # If adding this word plus spaces between words exceeds maxWidth, justify current line
            if num_of_letters + len(word) + len(line) > maxWidth:
                result.append(justify_line(line, num_of_letters, False))
                line = []
                num_of_letters = 0

            line.append(word)
            num_of_letters += len(word)

        # Justify the last line
        result.append(justify_line(line, num_of_letters, True))

        return result