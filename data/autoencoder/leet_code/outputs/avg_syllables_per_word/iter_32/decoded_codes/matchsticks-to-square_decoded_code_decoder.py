from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        side_length = total_length // 4
        matchsticks.sort(reverse=True)

        # Early pruning: if the largest stick is longer than side length, no solution
        if matchsticks and matchsticks[0] > side_length:
            return False

        sides = [0] * 4

        def can_form_sides(sides: List[int], index: int) -> bool:
            if index == len(matchsticks):
                # Check if all sides match side_length
                return all(side == side_length for side in sides)

            cur_match = matchsticks[index]
            for i in range(4):
                if sides[i] + cur_match <= side_length:
                    sides[i] += cur_match
                    if can_form_sides(sides, index + 1):
                        return True
                    sides[i] -= cur_match

                # If this side is still 0 after try, no need to try other sides that are also 0 
                # because it will be symmetric and hence wasteful
                if sides[i] == 0:
                    break

            return False

        return can_form_sides(sides, 0)