from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits):
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        def remove_digits(digit_list, times=1, need_count=1):
            # Remove 'times' digits from count if count[digit] >= need_count
            for d in digit_list:
                if count[d] >= need_count:
                    count[d] -= times
                    return True
            return False

        removed = False
        if remainder == 1:
            # Try removing one digit from [1,4,7]
            removed = remove_digits([1,4,7], times=1, need_count=1)
            if not removed:
                # Try removing two digits from [2,5,8]
                # Note: need_count=2 ensures at least two such digits can be removed
                removed = remove_digits([2,5,8], times=2, need_count=2)
        elif remainder == 2:
            # Try removing one digit from [2,5,8]
            removed = remove_digits([2,5,8], times=1, need_count=1)
            if not removed:
                # Try removing two digits from [1,4,7]
                removed = remove_digits([1,4,7], times=2, need_count=2)

        result = []
        for digit in range(9, -1, -1):
            result.extend([str(digit)] * count[digit])

        final_number = ''.join(result)

        if not final_number or final_number[0] == '0':
            return '0'
        else:
            return final_number