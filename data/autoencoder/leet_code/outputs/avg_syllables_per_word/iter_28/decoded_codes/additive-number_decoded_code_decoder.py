from typing import Optional

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def is_valid_sequence(start: int, first: int, second: int) -> bool:
            if start == n:
                return True
            expected = str(first + second)
            length = len(expected)
            if start + length > n or num[start:start + length] != expected:
                return False
            return is_valid_sequence(start + length, second, int(expected))

        for i in range(1, n // 2 + 1):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue
                if is_valid_sequence(j, int(first), int(second)):
                    return True
        return False