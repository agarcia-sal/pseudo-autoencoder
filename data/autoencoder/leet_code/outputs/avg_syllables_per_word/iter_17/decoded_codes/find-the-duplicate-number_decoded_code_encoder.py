from bisect import bisect_left

class Solution:
    def findDuplicate(self, list_of_numbers):
        def f(number_x):
            # Count how many elements in list_of_numbers are <= number_x
            return sum(v <= number_x for v in list_of_numbers) > number_x
        return bisect_left(range(len(list_of_numbers)), True, key=f)