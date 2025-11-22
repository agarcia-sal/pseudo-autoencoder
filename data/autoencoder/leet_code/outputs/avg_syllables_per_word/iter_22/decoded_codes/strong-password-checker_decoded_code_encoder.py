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
            if password[i] == password[i-1] == password[i-2]:
                length = 2
                # count length of repeating sequence
                while i < n and password[i] == password[i-1]:
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

            # delete from sequences that need one deletion to reduce a replacement
            dec = min(delete, one)
            replace -= dec
            delete -= dec

            # delete from sequences that need two deletions to reduce a replacement
            dec = min(delete, two * 2) // 2
            replace -= dec
            delete -= dec * 2

            # delete from sequences that need three deletions to reduce a replacement
            dec = delete // 3
            replace -= dec
            # delete -= dec * 3  # not needed after this use

            return (n - 20) + max(missing_types, replace)