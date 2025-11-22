class Solution:
    def checkSubarraySum(self, list_of_numbers, integer_k):
        remainder_map = {0: -1}
        current_sum = 0

        for i, num in enumerate(list_of_numbers):
            current_sum += num

            if integer_k != 0:
                current_sum %= integer_k

            if current_sum in remainder_map:
                if i - remainder_map[current_sum] > 1:
                    return True
            else:
                remainder_map[current_sum] = i

        return False