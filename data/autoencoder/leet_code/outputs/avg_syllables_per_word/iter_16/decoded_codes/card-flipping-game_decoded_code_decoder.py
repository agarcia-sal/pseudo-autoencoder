class Solution:
    def flipgame(self, fronts, backs):
        same = {f for f, b in zip(fronts, backs) if f == b}
        all_numbers = set(fronts) | set(backs)
        good_numbers = all_numbers - same
        if good_numbers:
            return min(good_numbers)
        else:
            return 0