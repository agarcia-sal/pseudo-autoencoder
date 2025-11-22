class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = any('a' <= c <= 'z' for c in password)
        has_upper = any('A' <= c <= 'Z' for c in password)
        has_digit = any(c.isdigit() for c in password)

        missing_types = 3 - (has_lower + has_upper + has_digit)

        replace = 0
        one = 0
        two = 0
        i = 2

        while i < n:
            if password[i] == password[i-1] == password[i-2]:
                length = 2
                # Count length of this repeated sequence
                while i < n and password[i] == password[i-1]:
                    length += 1
                    i += 1
                replace += length // 3
                mod = length % 3
                if mod == 0:
                    one += 1
                elif mod == 1:
                    two += 1
            else:
                i += 1

        if n < 6:
            return max(missing_types, 6 - n)
        elif n <= 20:
            return max(missing_types, replace)
        else:
            delete = n - 20

            # Use deletions to minimize replacements
            # Remove from sequences where length % 3 == 0 first (one)
            used = min(delete, one)
            replace -= used
            delete -= used

            # Remove from sequences where length % 3 == 1 next (two), each removal of 2 chars reduces a replace
            used = min(delete // 2, two)
            replace -= used
            delete -= used * 2

            # Remove from sequences where length % 3 == 2 last, each removal of 3 chars reduces a replace
            used = delete // 3
            replace -= used
            delete -= used * 3

            # replacements cannot be negative
            replace = max(replace, 0)

            return (n - 20) + max(missing_types, replace)