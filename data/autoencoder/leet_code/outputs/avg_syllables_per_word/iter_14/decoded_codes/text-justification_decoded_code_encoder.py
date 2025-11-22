class Solution:
    def fullJustify(self, words, maxWidth):
        def justify_line(line, num_of_letters, is_last_line):
            if len(line) == 1 or is_last_line:
                joined_line = ' '.join(line)
                number_of_spaces_to_add = maxWidth - num_of_letters - (len(line) - 1)
                justified_line = joined_line + ' ' * number_of_spaces_to_add
                return justified_line
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

                justified_line = ''.join(line)
                return justified_line

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