from typing import List

class Solution:
    def rob(self, list_of_numbers: List[int]) -> int:
        def rob_linear(list_of_houses: List[int]) -> int:
            if not list_of_houses:
                return 0
            if len(list_of_houses) == 1:
                return list_of_houses[0]

            dp_list = [0] * len(list_of_houses)
            dp_list[0] = list_of_houses[0]
            dp_list[1] = max(list_of_houses[0], list_of_houses[1])

            for index in range(2, len(list_of_houses)):
                dp_list[index] = max(dp_list[index - 1], dp_list[index - 2] + list_of_houses[index])

            return dp_list[-1]

        if not list_of_numbers:
            return 0
        if len(list_of_numbers) == 1:
            return list_of_numbers[0]

        return max(
            rob_linear(list_of_numbers[:-1]),
            rob_linear(list_of_numbers[1:])
        )