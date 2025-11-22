class Solution:
    def rotatedDigits(self, n: int) -> int:
        change_digits = {'2', '5', '6', '9'}
        same_digits = {'0', '1', '8'}

        def is_good_number(num: int) -> bool:
            num_str = str(num)
            allowed_digits = change_digits | same_digits
            if all(d in allowed_digits for d in num_str):
                return any(d in change_digits for d in num_str)
            return False

        good_count = sum(is_good_number(i) for i in range(1, n + 1))
        return good_count