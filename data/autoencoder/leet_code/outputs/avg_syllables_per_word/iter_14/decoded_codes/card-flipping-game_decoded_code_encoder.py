class Solution:
    def flipgame(self, fronts, backs):
        same = {x for x, y in zip(fronts, backs) if x == y}
        all_numbers = set(fronts) | set(backs)
        good_numbers = all_numbers - same
        return min(good_numbers) if good_numbers else 0