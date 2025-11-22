from typing import Set

class Solution:
    def rotatedDigits(self, n: int) -> int:
        change_digits: Set[str] = {'2', '5', '6', '9'}
        same_digits: Set[str] = {'0', '1', '8'}

        def is_good_number(num: int) -> bool:
            num_str = str(num)
            # Check all digits are in change_digits or same_digits
            if all(d in change_digits.union(same_digits) for d in num_str):
                # Check at least one digit is in change_digits
                if any(d in change_digits for d in num_str):
                    return True
            return False

        good_count = sum(1 for i in range(1, n + 1) if is_good_number(i))
        return good_count