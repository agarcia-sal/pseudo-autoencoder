sort_nums = sorted(nums)
start, end = -1, -2
for i in range(len(nums)):
    if nums[i] != sort_nums[i]:
        if start == -1:
            start = i
        end = i
return end - start + 1