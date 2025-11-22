class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid_sequence(start_position: int, first_number: int, second_number: int) -> bool:
            if start_position == len(num):
                return True

            expected_sum = first_number + second_number
            expected_string = str(expected_sum)
            expected_length = len(expected_string)

            if start_position + expected_length > len(num) or num[start_position:start_position + expected_length] != expected_string:
                return False

            return is_valid_sequence(start_position + expected_length, second_number, expected_sum)

        n = len(num)
        for i in range(1, n // 2 + 1):
            for j in range(i + 1, n):
                first_string = num[:i]
                second_string = num[i:j]

                if (len(first_string) > 1 and first_string[0] == '0') or (len(second_string) > 1 and second_string[0] == '0'):
                    continue

                if is_valid_sequence(j, int(first_string), int(second_string)):
                    return True

        return False