class Solution:
    def flipgame(self, fronts, backs):
        same = set()
        for front_element, back_element in zip(fronts, backs):
            if front_element == back_element:
                same.add(front_element)
        all_numbers = set(fronts) | set(backs)
        good_numbers = all_numbers - same
        if good_numbers:
            return min(good_numbers)
        else:
            return 0