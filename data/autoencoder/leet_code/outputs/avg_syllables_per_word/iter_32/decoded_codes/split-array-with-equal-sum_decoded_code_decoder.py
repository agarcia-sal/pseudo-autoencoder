from typing import List

class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 7:
            return False

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        # j splits the array into two parts with at least 3 elements on each side
        for j in range(3, n - 3):
            seen = set()
            # i is the first split point before j
            for i in range(1, j - 1):
                # sum(nums[0:i-1]) == sum(nums[i:j-1])
                if prefix_sum[i - 1] == prefix_sum[j - 1] - prefix_sum[i]:
                    seen.add(prefix_sum[i - 1])
            # k is the second split point after j
            for k in range(j + 2, n - 1):
                left = prefix_sum[k - 1] - prefix_sum[j]
                right = prefix_sum[-1] - prefix_sum[k]
                # sum(nums[j+1:k-1]) == sum(nums[k:n-1]) and that sum is in seen
                if left == right and left in seen:
                    return True

        return False