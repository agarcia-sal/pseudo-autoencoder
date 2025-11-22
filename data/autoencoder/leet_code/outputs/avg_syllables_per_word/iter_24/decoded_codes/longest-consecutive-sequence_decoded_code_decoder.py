class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        longest_streak = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                if current_streak > longest_streak:
                    longest_streak = current_streak
        return longest_streak