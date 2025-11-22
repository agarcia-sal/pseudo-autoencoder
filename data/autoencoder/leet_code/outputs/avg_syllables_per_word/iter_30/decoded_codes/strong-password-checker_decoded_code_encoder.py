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

        sum_types = 0
        if has_lower:
            sum_types += 1
        if has_upper:
            sum_types += 1
        if has_digit:
            sum_types += 1

        missing_types = 3 - sum_types

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

            decrease_replace_by_one = min(delete, one)
            replace -= decrease_replace_by_one

            decrease_replace_by_two = min(max(delete - decrease_replace_by_one, 0), two * 2)
            replace -= decrease_replace_by_two // 2

            decrease_replace_by_three = max(delete - decrease_replace_by_one - decrease_replace_by_two, 0)
            replace -= decrease_replace_by_three // 3

            return delete + max(missing_types, replace)