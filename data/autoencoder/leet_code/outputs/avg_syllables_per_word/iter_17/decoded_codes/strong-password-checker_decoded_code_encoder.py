class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = self.any_character_is_lowercase(password)
        has_upper = self.any_character_is_uppercase(password)
        has_digit = self.any_character_is_digit(password)

        missing_types = 3 - (has_lower + has_upper + has_digit)

        replace = 0
        one = 0
        two = 0
        i = 2

        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                # find length of run of identical characters
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

            # prioritize deletes in runs where length % 3 == 0
            reduce = min(delete, one)
            replace -= reduce
            delete -= reduce

            # prioritize deletes in runs where length % 3 == 1
            reduce = min(delete, two * 2) // 2
            replace -= reduce
            delete -= reduce * 2

            # prioritize deletes in runs where length % 3 == 2
            reduce = delete // 3
            replace -= reduce
            delete -= reduce * 3

            return (n - 20) + max(missing_types, replace)

    def any_character_is_lowercase(self, collection_of_characters) -> int:
        return any('a' <= c <= 'z' for c in collection_of_characters)

    def any_character_is_uppercase(self, collection_of_characters) -> int:
        return any('A' <= c <= 'Z' for c in collection_of_characters)

    def any_character_is_digit(self, collection_of_characters) -> int:
        return any('0' <= c <= '9' for c in collection_of_characters)