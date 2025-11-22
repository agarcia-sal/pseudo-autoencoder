class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = 3 - (has_lower + has_upper + has_digit)

        replace = 0  # total replacements needed for sequences of 3+ repeating chars
        one = 0      # count of sequences where (length % 3 == 0)
        two = 0      # count of sequences where (length % 3 == 1)

        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                # Move forward while characters keep repeating
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                replace += length // 3
                remainder = length % 3
                if remainder == 0:
                    one += 1
                elif remainder == 1:
                    two += 1
            else:
                i += 1

        if n < 6:
            return max(missing_types, 6 - n)
        elif n <= 20:
            return max(missing_types, replace)
        else:
            delete = n - 20
            # Use delete operations to reduce replacements needed
            # Prioritize sequences counted in 'one', then 'two', then the rest

            # Remove from sequences where length % 3 == 0
            reduce = min(delete, one)
            replace -= reduce
            delete -= reduce

            # Remove from sequences where length % 3 == 1 (need two deletes to reduce one replacement)
            reduce = min(max(delete, 0), two * 2) // 2
            replace -= reduce
            delete -= reduce * 2

            # Remove from remaining sequences (need three deletes to reduce one replacement)
            reduce = max(delete, 0) // 3
            replace -= reduce
            delete -= reduce * 3

            return (n - 20) + max(missing_types, replace)