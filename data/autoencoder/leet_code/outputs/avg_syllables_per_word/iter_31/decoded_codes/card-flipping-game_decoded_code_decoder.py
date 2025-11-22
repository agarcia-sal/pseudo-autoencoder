from typing import List, Set

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same: Set[int] = {x for x, y in zip(fronts, backs) if x == y}
        all_numbers: Set[int] = set(fronts) | set(backs)
        good_numbers: Set[int] = all_numbers - same
        return min(good_numbers) if good_numbers else 0