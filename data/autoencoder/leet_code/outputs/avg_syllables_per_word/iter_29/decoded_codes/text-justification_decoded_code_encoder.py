class Solution:
    def fullJustify(self, words, maxWidth):
        def justify_line(line, num_of_letters, is_last_line):
            if len(line) == 1 or is_last_line:
                # For single word or last line, left justify and pad spaces to the right
                spaces_to_add = maxWidth - num_of_letters - (len(line) - 1)
                return ' '.join(line) + ' ' * spaces_to_add
            else:
                total_spaces = maxWidth - num_of_letters
                number_of_gaps = len(line) - 1
                spaces_between_words = total_spaces // number_of_gaps
                extra_spaces = total_spaces % number_of_gaps
                for i in range(number_of_gaps):
                    if i < extra_spaces:
                        line[i] += ' ' * (spaces_between_words + 1)
                    else:
                        line[i] += ' ' * spaces_between_words
                return ''.join(line)

        result = []
        line = []
        num_of_letters = 0

        for word in words:
            current_line_length = num_of_letters + len(word) + len(line)
            if current_line_length > maxWidth:
                result.append(justify_line(line, num_of_letters, False))
                line = []
                num_of_letters = 0
            line.append(word)
            num_of_letters += len(word)

        result.append(justify_line(line, num_of_letters, True))
        return result