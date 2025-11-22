from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        pointer = Counter(s)
        digits = [0] * 10

        digits[0] = pointer.get('z', 0)  # zero
        digits[2] = pointer.get('w', 0)  # two
        digits[4] = pointer.get('u', 0)  # four
        digits[6] = pointer.get('x', 0)  # six
        digits[8] = pointer.get('g', 0)  # eight

        digits[3] = pointer.get('h', 0) - digits[8]  # three
        digits[5] = pointer.get('f', 0) - digits[4]  # five
        digits[7] = pointer.get('s', 0) - digits[6]  # seven

        digits[9] = pointer.get('i', 0) - digits[5] - digits[6] - digits[8]  # nine
        digits[1] = pointer.get('o', 0) - digits[0] - digits[2] - digits[4]  # one

        result = []
        for i in range(10):
            if digits[i] > 0:
                result.append(str(i) * digits[i])
        return ''.join(result)