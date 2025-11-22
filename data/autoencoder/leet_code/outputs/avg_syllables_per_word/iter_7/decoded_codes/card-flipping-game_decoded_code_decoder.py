from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {x for x, y in zip(fronts, backs) if x == y}
        all_numbers = set(fronts) | set(backs)
        good_numbers = all_numbers - same
        if good_numbers:
            return min(good_numbers)
        else:
            return 0