class Solution:
    def fullJustify(self, words, maxWidth):
        def justify_line(line, num_of_letters, is_last_line):
            if len(line) == 1 or is_last_line:
                # Left-justify: words separated by single spaces, pad the end with spaces
                return ' '.join(line) + ' ' * (maxWidth - num_of_letters - (len(line) - 1))
            else:
                total_spaces = maxWidth - num_of_letters
                num_of_gaps = len(line) - 1
                spaces_between_words = total_spaces // num_of_gaps
                extra_spaces = total_spaces % num_of_gaps

                for i in range(num_of_gaps):
                    # Append spaces to the word at index i
                    space_to_add = spaces_between_words + (1 if i < extra_spaces else 0)
                    line[i] += ' ' * space_to_add

                return ''.join(line)

        result = []
        line = []
        num_of_letters = 0

        for word in words:
            if num_of_letters + len(word) + len(line) > maxWidth:
                # justify current line (not last)
                result.append(justify_line(line, num_of_letters, False))
                line = []
                num_of_letters = 0
            line.append(word)
            num_of_letters += len(word)

        # justify last line
        result.append(justify_line(line, num_of_letters, True))
        return result