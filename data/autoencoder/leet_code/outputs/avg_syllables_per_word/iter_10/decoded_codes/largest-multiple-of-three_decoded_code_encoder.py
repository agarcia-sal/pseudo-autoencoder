from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits):
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        def remove_digits(rem, times=1):
            if rem == 1:
                singles = [1,4,7]
                doubles = [2,5,8]
            else:
                singles = [2,5,8]
                doubles = [1,4,7]

            for d in singles:
                if count[d] >= times:
                    count[d] -= times
                    return True
            if times == 1:
                for d in doubles:
                    if count[d] >= 2:
                        count[d] -= 2
                        return True
            return False

        if remainder == 1:
            if not remove_digits(1):
                remove_digits(1, 2)
        elif remainder == 2:
            if not remove_digits(2):
                remove_digits(2, 2)

        result = []
        for d in range(9, -1, -1):
            if count[d] > 0:
                result.append(str(d)*count[d])
        final_number = ''.join(result)

        if final_number and final_number[0] == '0':
            return "0"
        return final_number