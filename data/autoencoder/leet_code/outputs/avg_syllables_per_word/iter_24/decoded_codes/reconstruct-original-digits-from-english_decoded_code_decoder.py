from collections import Counter

class Solution:
    def originalDigits(self, s):
        count = Counter(s)
        digits = [0] * 10

        digits[0] = count.get('z', 0)
        digits[2] = count.get('w', 0)
        digits[4] = count.get('u', 0)
        digits[6] = count.get('x', 0)
        digits[8] = count.get('g', 0)

        digits[3] = count.get('h', 0) - digits[8]
        digits[5] = count.get('f', 0) - digits[4]
        digits[7] = count.get('s', 0) - digits[6]
        digits[9] = count.get('i', 0) - digits[5] - digits[6] - digits[8]
        digits[1] = count.get('o', 0) - digits[0] - digits[2] - digits[4]

        result = []
        for i in range(10):
            result.extend(str(i) * digits[i])

        return "".join(result)