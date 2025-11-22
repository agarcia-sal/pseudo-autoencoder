from collections import defaultdict

def numSubmatrixSumTarget(matrix, target):
    def subarraySum(nums, target):
        count = 0
        seen_sums = defaultdict(int)
        cum_sum = 0
        for num in nums:
            cum_sum += num
            if cum_sum == target:
                count += 1
            if (cum_sum - target) in seen_sums:
                count += seen_sums[cum_sum - target]
            seen_sums[cum_sum] += 1
        return count

    rows, cols = len(matrix), len(matrix[0])
    total_count = 0

    for top in range(rows):
        curr_cols = [0] * cols
        for bottom in range(top, rows):
            for col in range(cols):
                curr_cols[col] += matrix[bottom][col]
            total_count += subarraySum(curr_cols, target)

    return total_count