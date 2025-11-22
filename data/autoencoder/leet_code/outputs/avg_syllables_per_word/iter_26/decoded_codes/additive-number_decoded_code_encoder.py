class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid_sequence(start_position: int, first_number: int, second_number: int) -> bool:
            if start_position == len(num):
                return True

            expected_string = str(first_number + second_number)
            expected_length = len(expected_string)

            if start_position + expected_length > len(num) or num[start_position:start_position + expected_length] != expected_string:
                return False

            return is_valid_sequence(start_position + expected_length, second_number, int(expected_string))

        n = len(num)

        for i in range(1, n // 2 + 1):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]

                # Skip numbers with leading zeroes (except the number zero itself)
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue

                if is_valid_sequence(j, int(first), int(second)):
                    return True

        return False