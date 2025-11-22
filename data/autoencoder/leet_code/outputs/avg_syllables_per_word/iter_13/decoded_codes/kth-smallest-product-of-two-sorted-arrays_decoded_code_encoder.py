from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        nums2.sort()

        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # Count how many nums2[j] satisfy nums2[j] <= p / x
                    pos = bisect_right(nums2, p // x)
                    cnt += pos
                elif x < 0:
                    # Count how many nums2[j] satisfy nums2[j] >= ceil(p / x)
                    # Since x < 0, p / x <= 0 or so; use bisect_left for first >= value
                    val = (p + (-x - 1)) // x if p % x else p // x  # careful ceil division for negative divisor
                    pos = bisect_left(nums2, (p + (-x - 1)) // x if p % x else p // x)
                    # Actually simpler is just p//x if integer division is floor division in python (which it is),
                    # so bisect_left on p//x is fine.
                    pos = bisect_left(nums2, (p // x))
                    cnt += n - pos
                else:  # x == 0
                    cnt += n if p >= 0 else 0
            return cnt

        mx = max(abs(nums1[0]), abs(nums1[-1])) * max(abs(nums2[0]), abs(nums2[-1]))

        # Binary search over the range [-mx, mx]
        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left