class Solution:
    def flipgame(self, fronts, backs):
        same = set()
        for i in range(len(fronts)):
            x = fronts[i]
            y = backs[i]
            if x == y:
                same.add(x)
        all_numbers = set(fronts) | set(backs)
        good_numbers = all_numbers - same
        if good_numbers:
            return min(good_numbers)
        return 0