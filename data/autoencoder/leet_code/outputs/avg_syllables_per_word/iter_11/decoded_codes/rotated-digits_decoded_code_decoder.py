class Solution:
    def rotatedDigits(self, n: int) -> int:
        change_digits = {'2', '5', '6', '9'}
        same_digits = {'0', '1', '8'}

        def is_good_number(num: int) -> bool:
            num_str = str(num)
            if all(digit in change_digits or digit in same_digits for digit in num_str):
                return any(digit in change_digits for digit in num_str)
            return False

        good_count = 0
        for i in range(1, n + 1):
            if is_good_number(i):
                good_count += 1
        return good_count