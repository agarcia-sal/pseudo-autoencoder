class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        current_sequence = "1"

        for _ in range(1, n):
            next_sequence = []
            count = 1
            previous_char = current_sequence[0]

            for i in range(1, len(current_sequence)):
                if current_sequence[i] == previous_char:
                    count += 1
                else:
                    next_sequence.append(str(count))
                    next_sequence.append(previous_char)
                    previous_char = current_sequence[i]
                    count = 1

            next_sequence.append(str(count))
            next_sequence.append(previous_char)
            current_sequence = "".join(next_sequence)

        return current_sequence