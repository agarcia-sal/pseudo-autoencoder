def can_partition_k_subsets(nums, k):
    total_sum = sum(nums)
    if total_sum % k != 0:
        return False
    target = total_sum // k
    nums.sort(reverse=True)
    used = [False] * len(nums)

    def can_partition(i, k, curr_sum):
        if k == 0:
            return True
        if curr_sum == target:
            return can_partition(0, k - 1, 0)
        for j in range(i, len(nums)):
            if not used[j] and curr_sum + nums[j] <= target:
                used[j] = True
                if can_partition(j + 1, k, curr_sum + nums[j]):
                    return True
                used[j] = False
        return False

    return can_partition(0, k, 0)