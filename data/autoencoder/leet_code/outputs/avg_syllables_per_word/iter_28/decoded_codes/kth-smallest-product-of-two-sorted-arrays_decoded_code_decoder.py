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
                    # For negative x, p / x is negative division, careful with division rounding
                    # We want to find how many y in nums2 satisfy x*y <= p
                    # Since x is negative, inequality reverses:
                    # y >= ceiling(p / x)
                    # bisect_left finds first position >= that limit
                    val = (p + (-x) - 1) // x if p < 0 else p // x
                    pos = bisect_left(nums2, p // x)  # Correct in original approach
                    # But division toward negative infinity, so do integer division carefully
                    # Use float division
                    # Actually, p / x may not be integer dividing properly in python with //
                    # Let's convert to float for bisecting correctly:
                    threshold = p / x
                    pos = bisect_left(nums2, threshold)
                    cnt += n - pos
                else:
                    cnt += n if p >= 0 else 0
            return cnt

        min1, max1 = nums1[0], nums1[-1]
        min2, max2 = nums2[0], nums2[-1]
        mx = max(abs(min1), abs(max1)) * max(abs(min2), abs(max2))

        left, right = -mx, mx + 1
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left