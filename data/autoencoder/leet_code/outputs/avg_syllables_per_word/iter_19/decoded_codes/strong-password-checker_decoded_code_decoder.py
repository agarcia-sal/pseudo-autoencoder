class Solution:
    def strongPasswordChecker(self, password):
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
            # Use deletions to reduce replacements for sequences with mod 0
            use = min(delete, one)
            replace -= use
            delete -= use
            # Use deletions in pairs to reduce replacements for sequences with mod 1
            use = min(delete, two * 2)
            replace -= use // 2
            delete -= use
            # Use deletions in triplets to reduce replacements for other sequences
            use = max(delete, 0)
            replace -= use // 3
            return (n - 20) + max(missing_types, replace)