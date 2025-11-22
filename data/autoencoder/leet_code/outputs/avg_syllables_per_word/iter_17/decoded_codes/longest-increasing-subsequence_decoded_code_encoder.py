from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, list_of_numbers):
        if not list_of_numbers:
            return 0

        dp = []
        for number in list_of_numbers:
            insertion_index = bisect_left(dp, number)
            if insertion_index == len(dp):
                dp.append(number)
            else:
                dp[insertion_index] = number
        return len(dp)