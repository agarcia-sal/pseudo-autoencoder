class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        current_sequence = "1"
        for _ in range(2, n + 1):
            next_sequence = []
            count = 1
            previous_char = current_sequence[0]
            for ch in current_sequence[1:]:
                if ch == previous_char:
                    count += 1
                else:
                    next_sequence.append(str(count))
                    next_sequence.append(previous_char)
                    previous_char = ch
                    count = 1
            next_sequence.append(str(count))
            next_sequence.append(previous_char)
            current_sequence = "".join(next_sequence)
        return current_sequence