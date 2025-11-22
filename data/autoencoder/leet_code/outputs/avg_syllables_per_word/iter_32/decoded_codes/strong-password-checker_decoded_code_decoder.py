class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        # Check for presence of lowercase, uppercase and digit characters
        has_lower = any('a' <= c <= 'z' for c in password)
        has_upper = any('A' <= c <= 'Z' for c in password)
        has_digit = any(c.isdigit() for c in password)

        missing_types = 3 - (has_lower + has_upper + has_digit)

        replace = 0  # number of replacements needed for sequences of repeating characters
        one = 0      # count of sequences where (length % 3) == 0
        two = 0      # count of sequences where (length % 3) == 1

        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                # Move forward until end of sequence of identical chars
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
            # too short: fix missing types or length difference, whichever is higher
            return max(missing_types, 6 - n)
        elif n <= 20:
            # length is okay: fix missing types or replacements, whichever is higher
            return max(missing_types, replace)
        else:
            # length too long: need deletions
            delete = n - 20

            # Use deletions to reduce replacements

            # First, remove from sequences where len % 3 == 0
            use = min(delete, one)
            replace -= use
            delete -= use

            # Then, remove from sequences where len % 3 == 1
            use = min(max(delete, 0), two * 2)  # each such sequence needs 2 deletes to reduce one replacement
            replace -= use // 2
            delete -= use

            # Then, remove from sequences where len % 3 == 2
            use = max(delete, 0)
            replace -= use // 3
            delete -= use

            # After all deletions, replacements and missing types fix what's left
            return (n - 20) + max(missing_types, replace)