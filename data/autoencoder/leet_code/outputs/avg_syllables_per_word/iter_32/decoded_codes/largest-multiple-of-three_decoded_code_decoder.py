from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        if remainder == 1:
            # Try removing one digit with remainder 1 (1, 4, 7)
            for d in [1, 4, 7]:
                if count[d] > 0:
                    count[d] -= 1
                    break
            else:
                # Try removing two digits each with remainder 2 (2, 5, 8)
                for d in [2, 5, 8]:
                    if count[d] > 1:
                        count[d] -= 2
                        break
        elif remainder == 2:
            # Try removing one digit with remainder 2 (2, 5, 8)
            for d in [2, 5, 8]:
                if count[d] > 0:
                    count[d] -= 1
                    break
            else:
                # Try removing two digits each with remainder 1 (1, 4, 7)
                for d in [1, 4, 7]:
                    if count[d] > 1:
                        count[d] -= 2
                        break

        result = []
        for d in range(9, -1, -1):
            if count[d] > 0:
                result.append(str(d) * count[d])

        final_number = ''.join(result)
        # If final_number is non-empty and starts with '0', it means it's all zeros, return single '0'
        if final_number and final_number[0] == '0':
            return '0'
        return final_number