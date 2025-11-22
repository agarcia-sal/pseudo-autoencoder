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
                # Expand the sequence as long as characters match
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

            # Prioritize deletions to reduce replacements:
            # Remove one character from sequences where length % 3 == 0
            reduce = min(delete, one)
            replace -= reduce
            delete -= reduce

            # Remove two characters from sequences where length % 3 == 1
            reduce = min(delete, two * 2)
            replace -= reduce // 2
            delete -= reduce

            # Remove three characters from sequences where length % 3 == 2
            reduce = max(delete, 0)
            replace -= reduce // 3
            delete -= reduce

            return (n - 20) + max(missing_types, replace)