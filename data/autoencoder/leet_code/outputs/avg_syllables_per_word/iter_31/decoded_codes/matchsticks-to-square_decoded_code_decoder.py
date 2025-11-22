from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        side_length = total_length // 4
        matchsticks.sort(reverse=True)

        # Early pruning: if the longest matchstick is longer than side length, no square possible
        if matchsticks[0] > side_length:
            return False

        sides = [0] * 4

        def can_form_sides(sides: List[int], index: int) -> bool:
            if index == len(matchsticks):
                # All sides should be equal to side_length
                return all(side == side_length for side in sides)

            stick = matchsticks[index]
            for i in range(4):
                if sides[i] + stick <= side_length:
                    sides[i] += stick
                    if can_form_sides(sides, index + 1):
                        return True
                    sides[i] -= stick
                # If this side is 0 after trying to put stick, no point trying next empty side
                if sides[i] == 0:
                    break
            return False

        return can_form_sides(sides, 0)