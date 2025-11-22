from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = set()
        for f, b in zip(fronts, backs):
            if f == b:
                same.add(f)
        all_numbers = set(fronts) | set(backs)
        good_numbers = all_numbers - same
        return min(good_numbers) if good_numbers else 0