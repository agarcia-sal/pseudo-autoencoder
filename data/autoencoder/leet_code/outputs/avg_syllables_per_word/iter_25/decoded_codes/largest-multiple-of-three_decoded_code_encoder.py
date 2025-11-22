from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits):
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        def remove_digits(digits_to_remove, times=1):
            for d in digits_to_remove:
                if count[d] >= times:
                    count[d] -= times
                    return True
            return False

        if remainder == 1:
            if not remove_digits([1, 4, 7]):
                remove_digits([2, 5, 8], times=2)
        elif remainder == 2:
            if not remove_digits([2, 5, 8]):
                remove_digits([1, 4, 7], times=2)

        result = []
        for d in range(9, -1, -1):
            result.append(str(d) * count[d])

        final_number = ''.join(result)
        if final_number and final_number[0] == '0':
            return '0'
        return final_number