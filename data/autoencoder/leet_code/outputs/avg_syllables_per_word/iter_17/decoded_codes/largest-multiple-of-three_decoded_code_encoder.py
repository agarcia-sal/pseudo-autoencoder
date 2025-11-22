from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits):
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        def remove_digits(d_list, remove_count):
            for d in d_list:
                if count[d] >= remove_count:
                    count[d] -= remove_count
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
        for d in range(9, -1, -1):
            result.append(str(d) * count[d])

        final_number = "".join(result)

        if final_number and final_number[0] == '0':
            return "0"
        return final_number