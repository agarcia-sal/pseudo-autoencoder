def check_nums(nums):
    for i in range(len(nums)):
        if abs(nums[i] - i) > 1:
            return False
    return True