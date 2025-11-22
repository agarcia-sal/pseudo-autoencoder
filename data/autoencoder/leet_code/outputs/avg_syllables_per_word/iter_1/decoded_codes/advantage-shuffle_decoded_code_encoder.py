def advantage_count(nums1, nums2):
    nums1.sort()
    nums2_idx = sorted([(v, i) for i, v in enumerate(nums2)], reverse=True, key=lambda x: x[0])
    res = [0] * len(nums1)
    l, r = 0, len(nums1) - 1
    for v, i in nums2_idx:
        if nums1[r] > v:
            res[i] = nums1[r]
            r -= 1
        else:
            res[i] = nums1[l]
            l += 1
    return res