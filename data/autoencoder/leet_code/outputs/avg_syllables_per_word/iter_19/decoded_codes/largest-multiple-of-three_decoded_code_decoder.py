from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits):
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        if remainder == 1:
            # Try removing one digit with remainder 1
            for d in [1, 4, 7]:
                if count[d] > 0:
                    count[d] -= 1
                    break
            else:
                # Remove two digits with remainder 2
                removed = 0
                for d in [2, 5, 8]:
                    while count[d] > 0 and removed < 2:
                        count[d] -= 1
                        removed += 1
                    if removed == 2:
                        break

        elif remainder == 2:
            # Try removing one digit with remainder 2
            for d in [2, 5, 8]:
                if count[d] > 0:
                    count[d] -= 1
                    break
            else:
                # Remove two digits with remainder 1
                removed = 0
                for d in [1, 4, 7]:
                    while count[d] > 0 and removed < 2:
                        count[d] -= 1
                        removed += 1
                    if removed == 2:
                        break

        result = []
        for digit in range(9, -1, -1):
            if count[digit] > 0:
                result.append(str(digit) * count[digit])

        final_number = ''.join(result)
        if not final_number or final_number[0] == '0':
            return "0"
        return final_number