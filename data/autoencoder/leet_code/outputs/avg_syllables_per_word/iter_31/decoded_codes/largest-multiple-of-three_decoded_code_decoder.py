from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits):
        frequency = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        # Helper function to decrement frequency safely
        def decrement_freq(digits_list, count):
            for d in digits_list:
                if frequency[d] >= count:
                    frequency[d] -= count
                    return True
            return False

        if remainder == 1:
            # Try removing one digit with remainder 1 mod 3 (digits 1,4,7)
            if not decrement_freq([1, 4, 7], 1):
                # If not possible, remove two digits with remainder 2 mod 3 (2,5,8)
                decrement_freq([2, 5, 8], 2)
        elif remainder == 2:
            # Try removing one digit with remainder 2 mod 3
            if not decrement_freq([2, 5, 8], 1):
                # If not possible, remove two digits with remainder 1 mod 3
                decrement_freq([1, 4, 7], 2)

        result = []
        for d in range(9, -1, -1):
            result.append(str(d) * frequency[d])

        final_number = "".join(result)
        if final_number and final_number[0] == '0':
            return '0'
        return final_number