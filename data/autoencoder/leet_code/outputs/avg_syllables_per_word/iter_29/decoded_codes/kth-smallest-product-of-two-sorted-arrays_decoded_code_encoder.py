from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1_list, nums2_list, k):
        nums2_list.sort()  # ensure nums2_list is sorted for bisect operations
        n = len(nums2_list)

        def count(p):
            cnt = 0
            for x in nums1_list:
                if x > 0:
                    # count of nums2 elements <= p/x
                    cnt += bisect_right(nums2_list, p // x)
                elif x < 0:
                    # count of nums2 elements >= ceil(p/x)
                    # since bisect_left gives first position of element >= target
                    # n - pos gives count of elements >= target
                    val = (p + (-x) - 1) // x if p % x else p // x  # integer division ensuring floor division for negative denom
                    # but simpler: p/x is float, bisect does not take float precision, so use float division directly:
                    # Actually better to directly use p/x with float division:
                    import math
                    target = p / x  # x<0, p/x is float
                    pos = bisect_left(nums2_list, target)
                    cnt += n - pos
                else:  # x == 0
                    if p >= 0:
                        cnt += n
            return cnt

        mx = max(abs(nums1_list[0]), abs(nums1_list[-1])) * max(abs(nums2_list[0]), abs(nums2_list[-1]))
        left, right = -mx, mx + 1

        # binary search for smallest p such that count(p) >= k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left