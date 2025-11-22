class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = False
        has_upper = False
        has_digit = False

        for ch in password:
            if ch.islower():
                has_lower = True
            if ch.isupper():
                has_upper = True
            if ch.isdigit():
                has_digit = True

        missing_types = 3 - (has_lower + has_upper + has_digit)

        replace = 0
        one = 0
        two = 0
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                # Count the length of this sequence of the same character
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

            # prioritize removing characters from sequences that reduce replacements
            replace -= min(delete, one)
            delete -= min(delete, one)

            reduce_two = min(max(delete, 0) // 2, two)
            replace -= reduce_two
            delete -= reduce_two * 2

            reduce_three = max(delete, 0) // 3
            replace -= reduce_three
            # delete -= reduce_three * 3 # Not strictly necessary after this reduction

            return (n - 20) + max(missing_types, replace)