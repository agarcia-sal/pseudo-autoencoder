class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"

        current_sequence = "1"

        for _ in range(1, n):
            next_sequence = ""
            count = 1
            previous_char = current_sequence[0]

            for index in range(1, len(current_sequence)):
                if current_sequence[index] == previous_char:
                    count += 1
                else:
                    next_sequence += str(count)
                    next_sequence += previous_char
                    previous_char = current_sequence[index]
                    count = 1

            next_sequence += str(count)
            next_sequence += previous_char

            current_sequence = next_sequence

        return current_sequence