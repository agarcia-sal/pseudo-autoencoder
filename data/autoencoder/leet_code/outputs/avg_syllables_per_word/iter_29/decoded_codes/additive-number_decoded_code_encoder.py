class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid_sequence(start: int, first_num: int, second_num: int) -> bool:
            if start == len(num):
                return True

            sum_result = first_num + second_num
            expected_string = str(sum_result)
            expected_length = len(expected_string)

            if start + expected_length > len(num) or num[start:start + expected_length] != expected_string:
                return False

            return is_valid_sequence(start + expected_length, second_num, sum_result)

        total_length = len(num)
        for i in range(1, total_length // 2 + 1):
            for j in range(i + 1, total_length):
                first_substring = num[:i]
                second_substring = num[i:j]

                if (len(first_substring) > 1 and first_substring[0] == '0') or \
                   (len(second_substring) > 1 and second_substring[0] == '0'):
                    continue

                if is_valid_sequence(j, int(first_substring), int(second_substring)):
                    return True

        return False