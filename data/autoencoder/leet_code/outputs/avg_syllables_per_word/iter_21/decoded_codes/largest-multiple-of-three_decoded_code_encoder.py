from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits):
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        def remove_digits(digits_to_remove, times):
            for d in digits_to_remove:
                if count[d] >= times:
                    count[d] -= times
                    return True
            return False

        if remainder == 1:
            if not remove_digits([1, 4, 7], 1):
                remove_digits([2, 5, 8], 2)
        elif remainder == 2:
            if not remove_digits([2, 5, 8], 1):
                remove_digits([1, 4, 7], 2)

        result = []
        for digit in range(9, -1, -1):
            if count[digit] > 0:
                result.append(str(digit) * count[digit])

        final_number = ''.join(result)
        if not final_number or final_number[0] == '0':
            return '0'
        return final_number