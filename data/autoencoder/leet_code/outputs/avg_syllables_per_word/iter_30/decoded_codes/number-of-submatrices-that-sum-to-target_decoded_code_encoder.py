from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        def subarraySum(nums, target):
            count = 0
            seen_sums = defaultdict(int)
            cumulative_sum = 0
            for num in nums:
                cumulative_sum += num
                if cumulative_sum == target:
                    count += 1
                if (cumulative_sum - target) in seen_sums:
                    count += seen_sums[cumulative_sum - target]
                seen_sums[cumulative_sum] += 1
            return count

        rows = len(matrix)
        cols = len(matrix[0]) if matrix else 0
        total_count = 0

        for top in range(rows):
            current_cols = [0] * cols
            for bottom in range(top, rows):
                for col in range(cols):
                    current_cols[col] += matrix[bottom][col]
                total_count += subarraySum(current_cols, target)

        return total_count