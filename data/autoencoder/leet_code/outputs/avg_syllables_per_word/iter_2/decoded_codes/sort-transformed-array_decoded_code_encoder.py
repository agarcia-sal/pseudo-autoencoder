class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        def quadratic(x):
            return a * x * x + b * x + c

        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        if a >= 0:
            index = n - 1
            while left <= right:
                if quadratic(nums[left]) > quadratic(nums[right]):
                    result[index] = quadratic(nums[left])
                    left += 1
                else:
                    result[index] = quadratic(nums[right])
                    right -= 1
                index -= 1
        else:
            index = 0
            while left <= right:
                if quadratic(nums[left]) < quadratic(nums[right]):
                    result[index] = quadratic(nums[left])
                    left += 1
                else:
                    result[index] = quadratic(nums[right])
                    right -= 1
                index += 1

        return result