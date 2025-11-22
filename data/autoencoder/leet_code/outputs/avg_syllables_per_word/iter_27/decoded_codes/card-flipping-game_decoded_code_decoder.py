from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = set()
        for number_x, number_y in zip(fronts, backs):
            if number_x == number_y:
                same.add(number_x)
        all_numbers = set(fronts) | set(backs)
        good_numbers = all_numbers - same
        if good_numbers:
            return min(good_numbers)
        return 0