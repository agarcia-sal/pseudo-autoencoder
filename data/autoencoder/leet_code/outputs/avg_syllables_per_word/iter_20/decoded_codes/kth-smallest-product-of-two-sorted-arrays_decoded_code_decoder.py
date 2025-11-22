from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # Number of nums2[j] where x * nums2[j] <= p
                    # equivalent to nums2[j] <= p / x
                    pos = bisect_right(nums2, p / x)
                    cnt += pos
                elif x < 0:
                    # Number of nums2[j] where x * nums2[j] <= p
                    # nums2[j] >= ceil(p / x), since x<0, inequality reverses
                    pos = bisect_left(nums2, p / x)
                    cnt += n - pos
                else:  # x == 0
                    if p >= 0:
                        cnt += n
            return cnt

        mx = max(abs(nums1[0]), abs(nums1[-1])) * max(abs(nums2[0]), abs(nums2[-1]))
        left, right = -mx, mx

        # Binary search for minimal val such that count(val) >= k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left