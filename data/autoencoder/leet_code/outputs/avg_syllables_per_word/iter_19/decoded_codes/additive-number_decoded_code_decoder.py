class Solution:
    def isAdditiveNumber(self, num):
        def is_valid_sequence(start, first, second):
            if start == len(num):
                return True
            expected = str(first + second)
            length = len(expected)
            if start + length > len(num) or num[start:start + length] != expected:
                return False
            return is_valid_sequence(start + length, second, int(expected))

        n = len(num)
        for i in range(1, n // 2 + 1):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue
                if is_valid_sequence(j, int(first), int(second)):
                    return True
        return False