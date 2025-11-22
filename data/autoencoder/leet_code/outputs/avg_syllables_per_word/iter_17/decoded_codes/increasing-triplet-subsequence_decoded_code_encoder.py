from math import inf

class Solution:
    def increasingTriplet(self, list_of_numbers):
        first = inf
        second = inf
        for number in list_of_numbers:
            if number <= first:
                first = number
            elif number <= second:
                second = number
            else:
                return True
        return False