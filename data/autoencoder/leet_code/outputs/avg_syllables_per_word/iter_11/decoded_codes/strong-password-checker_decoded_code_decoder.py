class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = False
        has_upper = False
        has_digit = False
        for c in password:
            if c.islower():
                has_lower = True
            if c.isupper():
                has_upper = True
            if c.isdigit():
                has_digit = True

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

            reduce = min(delete, one)
            replace -= reduce
            delete -= reduce

            reduce = min(max(delete - 1, 0), two * 2)
            replace -= reduce // 2
            delete -= reduce

            reduce = max(delete - 2, 0)
            replace -= reduce // 3

            return (n - 20) + max(missing_types, replace)