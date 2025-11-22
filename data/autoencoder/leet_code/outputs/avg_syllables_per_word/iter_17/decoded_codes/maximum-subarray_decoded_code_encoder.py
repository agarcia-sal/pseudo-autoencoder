from typing import List

class Solution:
    def maxSubArray(self, list_of_numbers: List[int]) -> int:
        if not list_of_numbers:
            # Depending on context, might raise error or return 0 or None, here we return 0
            return 0
        maximum_sum = list_of_numbers[0]
        current_sum = list_of_numbers[0]
        for number in list_of_numbers[1:]:
            current_sum = max(number, current_sum + number)
            maximum_sum = max(maximum_sum, current_sum)
        return maximum_sum