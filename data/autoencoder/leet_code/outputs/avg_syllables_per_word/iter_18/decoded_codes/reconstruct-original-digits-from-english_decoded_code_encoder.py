from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        digits = [0] * 10
        digits[0] = count.get('z', 0)       # zero
        digits[2] = count.get('w', 0)       # two
        digits[4] = count.get('u', 0)       # four
        digits[6] = count.get('x', 0)       # six
        digits[8] = count.get('g', 0)       # eight
        digits[3] = count.get('h', 0) - digits[8]                 # three
        digits[5] = count.get('f', 0) - digits[4]                 # five
        digits[7] = count.get('s', 0) - digits[6]                 # seven
        digits[9] = count.get('i', 0) - digits[5] - digits[6] - digits[8]  # nine
        digits[1] = count.get('o', 0) - digits[0] - digits[2] - digits[4]  # one

        result = []
        for i in range(10):
            result.append(str(i) * digits[i])
        return ''.join(result)