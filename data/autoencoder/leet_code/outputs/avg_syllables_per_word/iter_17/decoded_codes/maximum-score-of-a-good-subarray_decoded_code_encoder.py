class Solution:
    def maximumScore(self, nums, k):
        left_pointer = k
        right_pointer = k
        current_minimum = nums[k]
        maximum_score = current_minimum

        n = len(nums)
        while left_pointer > 0 or right_pointer < n - 1:
            if left_pointer == 0:
                right_pointer += 1
            elif right_pointer == n - 1:
                left_pointer -= 1
            elif nums[left_pointer - 1] >= nums[right_pointer + 1]:
                left_pointer -= 1
            else:
                right_pointer += 1

            current_minimum = min(current_minimum, nums[left_pointer], nums[right_pointer])
            score_value = current_minimum * (right_pointer - left_pointer + 1)
            maximum_score = max(maximum_score, score_value)

        return maximum_score