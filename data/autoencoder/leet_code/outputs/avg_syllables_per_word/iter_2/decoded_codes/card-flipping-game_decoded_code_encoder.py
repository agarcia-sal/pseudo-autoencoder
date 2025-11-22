class Solution:
    def flipgame(self, fronts, backs):
        same = set()
        for x, y in zip(fronts, backs):
            if x == y:
                same.add(x)
        all_numbers = set(fronts) | set(backs)
        good_numbers = all_numbers - same
        if good_numbers:
            return min(good_numbers)
        else:
            return 0