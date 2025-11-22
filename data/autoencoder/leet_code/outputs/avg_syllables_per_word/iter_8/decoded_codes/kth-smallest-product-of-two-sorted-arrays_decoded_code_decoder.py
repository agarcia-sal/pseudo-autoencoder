import bisect

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # bisect_right returns insertion position on the right
                    cnt += bisect.bisect_right(nums2, p // x)
                elif x < 0:
                    # bisect_left returns insertion position on the left
                    cnt += n - bisect.bisect_left(nums2, (p + (-1 if p % x != 0 else 0)) // x)
                else:
                    cnt += n if p >= 0 else 0
            return cnt

        mx = max(abs(nums1[0]), abs(nums1[-1])) * max(abs(nums2[0]), abs(nums2[-1]))

        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left