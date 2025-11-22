from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        nums2.sort()

        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    cnt += bisect_right(nums2, p // x if p >= 0 else (p - x + 1) // x)
                elif x < 0:
                    # For negative x, p / x reverses inequality, careful with integer division
                    # Use float division then bisect accordingly
                    # To avoid float, we carefully adjust with math
                    # But here a direct approach with float: p/x
                    # Since nums2 is sorted ascending, and x<0, we want nums2[j] > p/x
                    # number of such j = n - bisect_left(nums2, p/x)
                    # p/x is float; bisect_left works with float
                    val = p / x
                    idx = bisect_left(nums2, val)
                    cnt += n - idx
                else:
                    cnt += n if p >= 0 else 0
            return cnt

        mx = max(abs(nums1[0]), abs(nums1[-1]))
        mx *= max(abs(nums2[0]), abs(nums2[-1]))

        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left