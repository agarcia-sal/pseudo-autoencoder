from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line: List[str], num_of_letters: int, is_last_line: bool) -> str:
            if len(line) == 1 or is_last_line:
                # Left justify: words separated by single spaces,
                # then pad with spaces to reach maxWidth
                line_str = ' '.join(line)
                return line_str + ' ' * (maxWidth - len(line_str))
            else:
                total_spaces = maxWidth - num_of_letters
                num_of_gaps = len(line) - 1
                spaces_between_words = total_spaces // num_of_gaps
                extra_spaces = total_spaces % num_of_gaps

                for i in range(num_of_gaps):
                    # Append spaces to the current word
                    # Add an extra space to the first 'extra_spaces' gaps
                    spaces_to_add = spaces_between_words + (1 if i < extra_spaces else 0)
                    line[i] += ' ' * spaces_to_add
                return ''.join(line)

        result = []
        line = []
        num_of_letters = 0

        for word in words:
            # Check if adding the next word exceeds maxWidth
            # Current line length includes spaces between words = len(line)
            if num_of_letters + len(word) + len(line) > maxWidth:
                result.append(justify_line(line, num_of_letters, False))
                line = []
                num_of_letters = 0
            line.append(word)
            num_of_letters += len(word)

        # Last line - left justify
        result.append(justify_line(line, num_of_letters, True))

        return result