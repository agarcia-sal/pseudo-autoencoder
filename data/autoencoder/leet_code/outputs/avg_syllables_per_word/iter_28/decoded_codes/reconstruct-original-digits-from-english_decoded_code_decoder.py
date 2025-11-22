from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)

        digits = [0] * 10

        digits[0] = count.get('Z', 0)
        digits[2] = count.get('W', 0)
        digits[4] = count.get('U', 0)
        digits[6] = count.get('X', 0)
        digits[8] = count.get('G', 0)

        digits[3] = count.get('H', 0) - digits[8]
        digits[5] = count.get('F', 0) - digits[4]
        digits[7] = count.get('S', 0) - digits[6]
        digits[9] = count.get('I', 0) - digits[5] - digits[6] - digits[8]
        digits[1] = count.get('O', 0) - digits[0] - digits[2] - digits[4]

        result = []
        for i in range(10):
            if digits[i] > 0:
                result.append(str(i) * digits[i])

        return ''.join(result)