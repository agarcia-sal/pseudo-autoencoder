from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        nums_str = list(map(str, nums))

        def compare(x, y):
            concatenation_one = y + x
            concatenation_two = x + y
            if concatenation_one > concatenation_two:
                return -1
            elif concatenation_one < concatenation_two:
                return 1
            else:
                return 0

        nums_str.sort(key=cmp_to_key(compare))
        if nums_str[0] == '0':
            return '0'
        return ''.join(nums_str)