class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        same = set()
        for x, y in zip(fronts, backs):
            if x == y:
                same.add(x)
        all_numbers = set(fronts) | set(backs)
        good_numbers = {num for num in all_numbers if num not in same}
        if good_numbers:
            return min(good_numbers)
        return 0