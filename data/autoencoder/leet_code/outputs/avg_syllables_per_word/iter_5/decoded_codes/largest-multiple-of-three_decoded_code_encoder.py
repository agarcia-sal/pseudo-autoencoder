from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits):
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        def remove_digits(to_remove, times):
            for d in to_remove:
                while count[d] > 0 and times > 0:
                    count[d] -= 1
                    times -= 1
                    if times == 0:
                        return True
            return False

        if remainder == 1:
            if not remove_digits([1,4,7], 1):
                remove_digits([2,5,8], 2)
        elif remainder == 2:
            if not remove_digits([2,5,8], 1):
                remove_digits([1,4,7], 2)

        result = []
        for d in range(9, -1, -1):
            result.append(str(d) * count[d])

        final_number = ''.join(result)
        if not final_number or final_number[0] == '0':
            return '0'
        return final_number