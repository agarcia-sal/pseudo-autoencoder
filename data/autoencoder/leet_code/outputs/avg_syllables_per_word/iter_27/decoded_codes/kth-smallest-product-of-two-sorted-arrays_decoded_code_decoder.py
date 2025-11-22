from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # count how many nums2[j] <= p/x
                    pos = bisect_right(nums2, p // x)
                    cnt += pos
                elif x < 0:
                    # count how many nums2[j] >= ceil(p/x)
                    # since p/x might be float division, use division cautiously
                    # p/x might not be integer division, so use float division and adjust
                    val = p / x
                    pos = bisect_left(nums2, val)
                    cnt += n - pos
                else:  # x == 0
                    if p >= 0:
                        cnt += n  # zero * any number = 0 which is <= p if p >= 0
            return cnt

        # compute bounds for binary search based on extremes of nums1 and nums2
        max_abs_num1 = max(abs(nums1[0]), abs(nums1[-1]))
        max_abs_num2 = max(abs(nums2[0]), abs(nums2[-1]))
        mx = max_abs_num1 * max_abs_num2

        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left