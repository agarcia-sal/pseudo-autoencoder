from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        def remove_digits(to_remove, amount):
            for d in to_remove:
                if count[d] >= amount:
                    count[d] -= amount
                    return True
            return False

        if remainder == 1:
            removed = remove_digits([1, 4, 7], 1)
            if not removed:
                remove_digits([2, 5, 8], 2)
        elif remainder == 2:
            removed = remove_digits([2, 5, 8], 1)
            if not removed:
                remove_digits([1, 4, 7], 2)

        result = []
        for digit in range(9, -1, -1):
            if count[digit] > 0:
                result.append(str(digit) * count[digit])

        final_number = ''.join(result)
        if final_number and final_number[0] == '0':
            return '0'
        return final_number