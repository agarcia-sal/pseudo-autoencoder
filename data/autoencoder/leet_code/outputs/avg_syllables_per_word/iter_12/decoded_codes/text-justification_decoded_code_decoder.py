class Solution:
    def fullJustify(self, words, maxWidth):
        def justify_line(line, num_of_letters, is_last_line):
            if len(line) == 1 or is_last_line:
                # Left justify: words joined by single spaces, pad right with spaces
                line_str = ' '.join(line)
                return line_str + ' ' * (maxWidth - len(line_str))
            else:
                total_spaces = maxWidth - num_of_letters
                num_of_gaps = len(line) - 1
                spaces_between_words = total_spaces // num_of_gaps
                extra_spaces = total_spaces % num_of_gaps

                justified_line = []
                for i in range(num_of_gaps):
                    justified_line.append(line[i])
                    # Append spaces: one extra for the first extra_spaces gaps
                    spaces_to_add = spaces_between_words + (1 if i < extra_spaces else 0)
                    justified_line.append(' ' * spaces_to_add)
                justified_line.append(line[-1])

                return ''.join(justified_line)

        result = []
        line = []
        num_of_letters = 0

        for word in words:
            # Check if adding the new word exceeds maxWidth (consider spaces between words)
            if num_of_letters + len(word) + len(line) > maxWidth:
                result.append(justify_line(line, num_of_letters, False))
                line = []
                num_of_letters = 0
            line.append(word)
            num_of_letters += len(word)

        # Last line
        result.append(justify_line(line, num_of_letters, True))

        return result