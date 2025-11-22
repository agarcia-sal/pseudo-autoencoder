class Solution:
    def flipgame(self, fronts, backs):
        same = {x for x, y in zip(fronts, backs) if x == y}
        good_numbers = set(fronts) | set(backs) - same
        return min(good_numbers) if good_numbers else 0