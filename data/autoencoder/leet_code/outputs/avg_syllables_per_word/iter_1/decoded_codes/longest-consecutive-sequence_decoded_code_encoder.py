def longestConsecutive(nums):
    if not nums:
        return 0
    numSet = set(nums)
    longest = 0
    for num in numSet:
        if num - 1 not in numSet:
            length = 1
            while num + length in numSet:
                length += 1
            longest = max(longest, length)
    return longest