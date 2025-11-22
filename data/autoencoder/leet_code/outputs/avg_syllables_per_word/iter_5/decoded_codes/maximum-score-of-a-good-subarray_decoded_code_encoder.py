class Solution:
    def maximumScore(self, nums, k):
        left, right = k, k
        current_min = nums[k]
        max_score = current_min

        while left > 0 or right < len(nums) - 1:
            if left == 0:
                right += 1
            elif right == len(nums) - 1:
                left -= 1
            elif nums[left - 1] >= nums[right + 1]:
                left -= 1
            else:
                right += 1

            current_min = min(current_min, nums[left], nums[right])
            max_score = max(max_score, current_min * (right - left + 1))

        return max_score