class Solution:
    def splitArray(self, nums):
        n = len(nums)
        if n < 7:
            return False

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        for j in range(3, n - 3):
            seen = set()
            for i in range(1, j - 1):
                left_sum = prefix_sum[i - 1]
                mid_sum = prefix_sum[j - 1] - prefix_sum[i]
                if left_sum == mid_sum:
                    seen.add(left_sum)

            for k in range(j + 2, n - 1):
                right_sum = prefix_sum[n - 1] - prefix_sum[k]
                mid_right_sum = prefix_sum[k - 1] - prefix_sum[j]
                if right_sum == mid_right_sum and mid_right_sum in seen:
                    return True

        return False