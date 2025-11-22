class Solution:
    def minimumMountainRemovals(self, nums):
        n = len(nums)

        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    value = lis[j] + 1
                    if value > lis[i]:
                        lis[i] = value

        lds = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    value = lds[j] + 1
                    if value > lds[i]:
                        lds[i] = value

        max_mountain_length = 0
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                combined_length = lis[i] + lds[i] - 1
                if combined_length > max_mountain_length:
                    max_mountain_length = combined_length

        return n - max_mountain_length