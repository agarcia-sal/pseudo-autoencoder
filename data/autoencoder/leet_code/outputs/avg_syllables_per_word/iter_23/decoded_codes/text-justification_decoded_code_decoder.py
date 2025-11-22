from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line: List[str], num_of_letters: int, is_last_line: bool) -> str:
            if len(line) == 1 or is_last_line:
                # For last line or single word line: left-justified, fill the rest with spaces
                return ' '.join(line) + ' ' * (maxWidth - num_of_letters - (len(line) - 1))
            else:
                total_spaces = maxWidth - num_of_letters
                num_of_gaps = len(line) - 1
                spaces_between_words = total_spaces // num_of_gaps
                extra_spaces = total_spaces % num_of_gaps

                # Append spaces to the words except the last one
                for i in range(num_of_gaps):
                    # if i < extra_spaces, add one extra space
                    spaces_to_add = spaces_between_words + (1 if i < extra_spaces else 0)
                    line[i] += ' ' * spaces_to_add
                return ''.join(line)

        result = []
        line = []
        num_of_letters = 0

        for word in words:
            # If adding this word plus spaces between words exceeds maxWidth,
            # justify the current line and start a new one
            if num_of_letters + len(word) + len(line) > maxWidth:
                result.append(justify_line(line, num_of_letters, False))
                line = []
                num_of_letters = 0
            line.append(word)
            num_of_letters += len(word)

        # Last line - left justified
        result.append(justify_line(line, num_of_letters, True))

        return result