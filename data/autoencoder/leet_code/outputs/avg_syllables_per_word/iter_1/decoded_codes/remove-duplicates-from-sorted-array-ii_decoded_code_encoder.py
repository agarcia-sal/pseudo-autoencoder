def remove_duplicates(nums):
    if not nums:
        return 0
    write = 0
    for i in range(min(2, len(nums))):
        nums[write] = nums[i]
        write += 1
    for i in range(2, len(nums)):
        if nums[i] != nums[write - 2]:
            nums[write] = nums[i]
            write += 1
    return write