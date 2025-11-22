from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        side_length = total_length // 4
        matchsticks.sort(reverse=True)

        def can_form_sides(list_of_sides: List[int], index: int) -> bool:
            if index == len(matchsticks):
                return all(side == side_length for side in list_of_sides)

            for position in range(4):
                if list_of_sides[position] + matchsticks[index] <= side_length:
                    list_of_sides[position] += matchsticks[index]
                    if can_form_sides(list_of_sides, index + 1):
                        return True
                    list_of_sides[position] -= matchsticks[index]
                if list_of_sides[position] == 0:
                    break
            return False

        return can_form_sides([0, 0, 0, 0], 0)