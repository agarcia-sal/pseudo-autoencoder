class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        current_sequence = "1"

        for _ in range(2, n + 1):
            next_sequence = ""
            count = 1
            previous_char = current_sequence[0]

            for i in range(1, len(current_sequence)):
                if current_sequence[i] == previous_char:
                    count += 1
                else:
                    next_sequence = self.AppendCountAndChar(count, previous_char, next_sequence)
                    previous_char = current_sequence[i]
                    count = 1

            next_sequence = self.AppendCountAndChar(count, previous_char, next_sequence)

            current_sequence = next_sequence

        return current_sequence

    def AppendCountAndChar(self, count: int, character: str, sequence: str) -> str:
        count_string = self.ConvertNumberToString(count)
        new_sequence = sequence + count_string + character
        return new_sequence

    def ConvertNumberToString(self, number: int) -> str:
        return str(number)