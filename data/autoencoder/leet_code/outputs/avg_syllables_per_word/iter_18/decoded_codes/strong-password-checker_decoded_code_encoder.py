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
                # Count length of repeating sequence
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

            # Prioritize reducing replace using deletions:
            # First remove one character sequences
            reduce = min(delete, one)
            replace -= reduce
            delete -= reduce

            # Then remove two character sequences (each delete reduces replace by 1 for every 2 deletes)
            reduce = min(max(delete, 0), two * 2) // 2
            replace -= reduce
            delete -= reduce * 2

            # Then remove three character sequences (each delete reduces replace by 1 for every 3 deletes)
            reduce = max(delete, 0) // 3
            replace -= reduce

            return (n - 20) + max(missing_types, replace)