class Solution:
    def fullJustify(self, words, maxWidth):
        def justify_line(line, num_of_letters, is_last_line):
            if len(line) == 1 or is_last_line:
                return ' '.join(line) + ' ' * (maxWidth - num_of_letters - (len(line) - 1))
            total_spaces = maxWidth - num_of_letters
            num_of_gaps = len(line) - 1
            spaces_between_words = total_spaces // num_of_gaps
            extra_spaces = total_spaces % num_of_gaps

            justified = []
            for i in range(num_of_gaps):
                justified.append(line[i])
                justified.append(' ' * (spaces_between_words + (1 if i < extra_spaces else 0)))
            justified.append(line[-1])
            return ''.join(justified)

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