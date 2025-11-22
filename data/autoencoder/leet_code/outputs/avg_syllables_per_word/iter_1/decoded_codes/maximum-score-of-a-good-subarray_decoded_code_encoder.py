def max_score(nums, k):
    l = r = k
    cur_min = nums[k]
    max_score = cur_min

    while l > 0 or r < len(nums) - 1:
        if l == 0:
            r += 1
        elif r == len(nums) - 1:
            l -= 1
        elif nums[l - 1] >= nums[r + 1]:
            l -= 1
        else:
            r += 1

        cur_min = min(cur_min, nums[l], nums[r])
        score = cur_min * (r - l + 1)
        max_score = max(max_score, score)

    return max_score