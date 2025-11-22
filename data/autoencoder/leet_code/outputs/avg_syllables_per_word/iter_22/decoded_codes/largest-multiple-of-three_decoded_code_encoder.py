from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits) -> str:
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        if remainder == 1:
            for digit_element in [1, 4, 7]:
                if count[digit_element] > 0:
                    count[digit_element] -= 1
                    break
            else:
                for digit_element in [2, 5, 8]:
                    if count[digit_element] > 1:
                        count[digit_element] -= 2
                        break

        if remainder == 2:
            for digit_element in [2, 5, 8]:
                if count[digit_element] > 0:
                    count[digit_element] -= 1
                    break
            else:
                for digit_element in [1, 4, 7]:
                    if count[digit_element] > 1:
                        count[digit_element] -= 2
                        break

        result = []
        for digit_value in range(9, -1, -1):
            result.append(str(digit_value) * count[digit_value])

        final_number = ''.join(result)

        if final_number and final_number[0] == '0':
            return '0'
        else:
            return final_number