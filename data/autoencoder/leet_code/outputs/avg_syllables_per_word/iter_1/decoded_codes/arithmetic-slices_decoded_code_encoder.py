def number_of_arithmetic_slices(nums):
    if len(nums) < 3:
        return 0
    total, length = 0, 2
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            length += 1
            total += length - 2
        else:
            length = 2
    return total