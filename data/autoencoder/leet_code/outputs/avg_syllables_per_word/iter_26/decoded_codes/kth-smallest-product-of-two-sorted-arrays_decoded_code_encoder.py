import bisect

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # Count of nums2 elements <= p / x
                    cnt += bisect.bisect_right(nums2, p // x)
                elif x < 0:
                    # Count of nums2 elements >= ceil(p / x)
                    # Since nums2 is sorted ascending, position to the left of (p // x)
                    pos = bisect.bisect_left(nums2, (p + (-1 if p % x != 0 else 0)) // x)
                    cnt += n - pos
                else:
                    # x == 0
                    cnt += n if p >= 0 else 0
            return cnt

        n1, n2 = len(nums1), len(nums2)
        # Compute maximum absolute value for boundary
        mx1 = max(abs(nums1[0]), abs(nums1[-1]))
        mx2 = max(abs(nums2[0]), abs(nums2[-1]))
        mx = mx1 * mx2

        # Binary search for the kth product
        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left