class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid_sequence(start: int, first: int, second: int) -> bool:
            if start == len(num):
                return True
            expected_number_string = str(first + second)
            expected_length = len(expected_number_string)
            if start + expected_length > len(num) or num[start:start + expected_length] != expected_number_string:
                return False
            return is_valid_sequence(start + expected_length, second, int(expected_number_string))

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