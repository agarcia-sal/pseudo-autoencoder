class Solution:
    def arrayNesting(self, nums):
        visited = [False] * len(nums)
        max_length = 0

        for i in range(len(nums)):
            if not visited[i]:
                current_length = 0
                k = i
                while not visited[k]:
                    visited[k] = True
                    k = nums[k]
                    current_length += 1
                if current_length > max_length:
                    max_length = current_length

        return max_length