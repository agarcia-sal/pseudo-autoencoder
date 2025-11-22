from math import inf

class Solution:
    def increasingTriplet(self, nums):
        first = inf
        second = inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False