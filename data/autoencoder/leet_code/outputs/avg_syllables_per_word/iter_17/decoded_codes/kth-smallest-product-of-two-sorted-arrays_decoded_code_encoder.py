import bisect

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # Count how many nums2 elements satisfy x * y <= p
                    cnt += bisect.bisect_right(nums2, p // x)
                elif x < 0:
                    # Count elements where product <= p for negative x
                    cnt += n - bisect.bisect_left(nums2, (p // x) + (1 if p % x else 0))
                else:  # x == 0
                    cnt += n if p >= 0 else 0
            return cnt

        mx = max(abs(nums1[0]), abs(nums1[-1]))
        mx *= max(abs(nums2[0]), abs(nums2[-1]))

        # Binary search over the product range [-mx, mx]
        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left