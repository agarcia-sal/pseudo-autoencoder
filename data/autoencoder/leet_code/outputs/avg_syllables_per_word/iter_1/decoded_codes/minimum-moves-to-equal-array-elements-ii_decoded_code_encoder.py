def min_moves_to_equal_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves