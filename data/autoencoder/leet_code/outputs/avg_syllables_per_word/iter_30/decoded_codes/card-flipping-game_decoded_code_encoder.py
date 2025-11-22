class Solution:
    def flipgame(self, fronts, backs):
        same = set()
        for x, y in zip(fronts, backs):
            if x == y:
                same.add(x)
        all_numbers = fronts + backs
        good_numbers = [num for num in all_numbers if num not in same]
        if good_numbers:
            return min(good_numbers)
        else:
            return 0