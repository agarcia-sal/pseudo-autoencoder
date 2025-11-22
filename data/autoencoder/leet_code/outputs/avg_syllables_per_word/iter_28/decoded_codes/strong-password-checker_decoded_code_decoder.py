from typing import Optional


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)

        missing_types = 3 - (has_lower + has_upper + has_digit)

        replace = 0
        one = 0
        two = 0
        i = 2

        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                replace += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                i += 1

        if n < 6:
            return max(missing_types, 6 - n)
        elif n <= 20:
            return max(missing_types, replace)
        else:
            delete = n - 20

            # Reduce replacements by removing one character from sequences where length % 3 == 0
            reduce = min(delete, one)
            replace -= reduce
            delete -= reduce

            # Reduce replacements by removing two chars from sequences where length % 3 == 1
            reduce = min(delete // 2, two)
            replace -= reduce
            delete -= reduce * 2

            # Reduce replacements by removing three chars from the rest sequences
            reduce = delete // 3
            replace -= reduce
            delete -= reduce * 3

            return (n - 20) + max(missing_types, replace)