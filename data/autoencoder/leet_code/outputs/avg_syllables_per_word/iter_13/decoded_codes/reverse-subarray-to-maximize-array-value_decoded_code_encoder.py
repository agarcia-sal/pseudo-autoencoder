class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 2:
            return abs(nums[0] - nums[1])

        initial_value = 0
        for i in range(1, n):
            initial_value += abs(nums[i] - nums[i - 1])

        max_edge_gain = 0
        for i in range(1, n):
            edge_gain = abs(nums[0] - nums[i]) - abs(nums[i] - nums[i - 1])
            if edge_gain > max_edge_gain:
                max_edge_gain = edge_gain

        for i in range(n - 1):
            edge_gain = abs(nums[-1] - nums[i]) - abs(nums[i + 1] - nums[i])
            if edge_gain > max_edge_gain:
                max_edge_gain = edge_gain

        min_pair = min(max(nums[i], nums[i + 1]) for i in range(n - 1))
        max_pair = max(min(nums[i], nums[i + 1]) for i in range(n - 1))

        general_gain = max(0, 2 * (max_pair - min_pair))

        return initial_value + max(max_edge_gain, general_gain)