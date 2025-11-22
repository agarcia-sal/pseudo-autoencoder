class Solution:
    def flipgame(self, fronts, backs):
        same = set()
        for x, y in zip(fronts, backs):
            if x == y:
                same.add(x)
        all_numbers = set(fronts) | set(backs)
        good_numbers = {num for num in all_numbers if num not in same}
        return min(good_numbers) if good_numbers else 0