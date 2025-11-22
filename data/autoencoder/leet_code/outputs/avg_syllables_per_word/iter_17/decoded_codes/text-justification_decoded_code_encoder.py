from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line: List[str], num_of_letters: int, is_last_line: bool) -> str:
            # Helper to append spaces to a word
            def append_spaces(word: str, count: int) -> str:
                return word + ' ' * count

            if len(line) == 1 or is_last_line:
                # Left-justify: words joined by single space, then pad right with spaces
                line_str = ' '.join(line)
                # Calculate remaining spaces to reach maxWidth
                remaining = maxWidth - len(line_str)
                return line_str + ' ' * remaining
            else:
                total_spaces = maxWidth - num_of_letters
                num_gaps = len(line) - 1
                spaces_between_words = total_spaces // num_gaps
                extra_spaces = total_spaces % num_gaps

                # Build justified line
                justified_words = []
                for i in range(num_gaps):
                    space_count = spaces_between_words + (1 if i < extra_spaces else 0)
                    justified_words.append(append_spaces(line[i], space_count))
                justified_words.append(line[-1])

                return ''.join(justified_words)

        result = []
        line = []
        num_of_letters = 0

        for word in words:
            # Check if adding this word exceeds maxWidth (account for spaces between words)
            if num_of_letters + len(word) + len(line) > maxWidth:
                result.append(justify_line(line, num_of_letters, False))
                line = []
                num_of_letters = 0
            line.append(word)
            num_of_letters += len(word)

        # Last line is left-justified
        result.append(justify_line(line, num_of_letters, True))

        return result