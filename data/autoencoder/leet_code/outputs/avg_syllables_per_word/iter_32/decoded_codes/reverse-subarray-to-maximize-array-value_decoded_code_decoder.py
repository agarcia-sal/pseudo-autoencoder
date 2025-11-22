from typing import List

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return abs(nums[0] - nums[1])

        # Calculate initial sum of absolute differences
        initial_value = 0
        for i in range(1, n):
            initial_value += abs(nums[i] - nums[i - 1])

        max_edge_gain = 0

        # Check reversing subarray that includes the first element
        for i in range(1, n):
            # Gain from replacing edge (nums[i] - nums[i-1]) with (nums[i] - nums[0])
            edge_gain_candidate = abs(nums[0] - nums[i]) - abs(nums[i] - nums[i - 1])
            if edge_gain_candidate > max_edge_gain:
                max_edge_gain = edge_gain_candidate

        # Check reversing subarray that includes the last element
        for i in range(n - 1):
            # Gain from replacing edge (nums[i+1] - nums[i]) with (nums[n-1] - nums[i])
            edge_gain_candidate = abs(nums[-1] - nums[i]) - abs(nums[i + 1] - nums[i])
            if edge_gain_candidate > max_edge_gain:
                max_edge_gain = edge_gain_candidate

        # Find min of max pairs and max of min pairs adjacent elements
        min_pair = float('inf')
        max_pair = float('-inf')
        for i in range(n - 1):
            high = max(nums[i], nums[i + 1])
            low = min(nums[i], nums[i + 1])
            if high < min_pair:
                min_pair = high
            if low > max_pair:
                max_pair = low

        # General gain from reversing some subarray (not necessarily involving edges)
        general_gain = max(0, 2 * (max_pair - min_pair))

        return initial_value + max(max_edge_gain, general_gain)