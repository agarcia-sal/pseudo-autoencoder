from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # count how many nums2[j] <= p / x
                    pos = bisect_right(nums2, p // x if p >= 0 else (p - x + 1) // x)
                    cnt += pos
                elif x < 0:
                    # count how many nums2[j] >= ceil(p / x)
                    # Since x<0, division and comparison flips:
                    val = p / x
                    # To find left position for val in nums2 for counting >= val:
                    pos = bisect_left(nums2, val)
                    cnt += n - pos
                else:
                    # x == 0
                    if p >= 0:
                        cnt += n
            return cnt

        max_abs_nums1 = max(abs(nums1[0]), abs(nums1[-1]))
        max_abs_nums2 = max(abs(nums2[0]), abs(nums2[-1]))
        mx = max_abs_nums1 * max_abs_nums2

        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left