import string

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)

        missing_types = 3 - (has_lower + has_upper + has_digit)

        replace = 0  # total replacements needed for sequences of repeated chars
        one = 0      # count of sequences with (length % 3) == 0
        two = 0      # count of sequences with (length % 3) == 1

        i = 2
        while i < n:
            if password[i] == password[i -1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i -1]:
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
            # Use deletions to reduce replace counts from sequences optimally:
            # First reduce sequences where length % 3 == 0, remove 1 char per seq reduces replace by 1
            reduce_one = min(delete, one)
            replace -= reduce_one
            delete -= reduce_one

            # Then sequences where length % 3 == 1, removing 2 chars reduces replace by 1
            reduce_two = min(delete // 2, two)
            replace -= reduce_two
            delete -= reduce_two * 2

            # Lastly sequences where length % 3 == 2 (or others). Removing 3 chars reduces replace by 1 each time
            reduce_three = delete // 3
            replace -= reduce_three
            delete -= reduce_three * 3

            if replace < 0:
                replace = 0

            return (n - 20) + max(missing_types, replace)