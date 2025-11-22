from bisect import bisect_left, bisect_right

def kthSmallestProduct(nums1, nums2, k):
    def count(p):
        c, n = 0, len(nums2)
        for x in nums1:
            if x > 0:
                c += bisect_right(nums2, p / x)
            elif x < 0:
                c += n - bisect_left(nums2, p / x)
            else:
                c += n if p >= 0 else 0
        return c

    mx = max(abs(nums1[0]), abs(nums1[-1])) * max(abs(nums2[0]), abs(nums2[-1]))

    left, right = -mx, mx
    while left < right:
        mid = (left + right) // 2
        if count(mid) >= k:
            right = mid
        else:
            left = mid + 1
    return left