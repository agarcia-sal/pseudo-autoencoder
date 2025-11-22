from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        nums2_sorted = nums2  # assume nums2 is already sorted as per the problem statement

        def count(p):
            cnt = 0
            n = len(nums2_sorted)
            for x in nums1:
                if x > 0:
                    # number of nums2 elements <= p // x
                    cnt += bisect_right(nums2_sorted, p // x)
                elif x < 0:
                    # number of nums2 elements >= ceil(p / x) == n - bisect_left(nums2, p / x)
                    # since p / x might not be integer, use float division and bisect_left
                    # to find first element >= p / x
                    # p // x truncates towards negative infinity for ints but p/x float division is needed
                    cnt += n - bisect_left(nums2_sorted, -((-p) / x) if x < 0 else p / x)
                    # Above is complicated, let's just do float division explicitly:
                    val = p / x
                    cnt += n - bisect_left(nums2_sorted, val)
                else:  # x == 0
                    if p >= 0:
                        cnt += n
            return cnt

        abs_nums1_0 = abs(nums1[0])
        abs_nums1_last = abs(nums1[-1])
        abs_nums2_0 = abs(nums2[0])
        abs_nums2_last = abs(nums2[-1])
        mx = max(abs_nums1_0, abs_nums1_last) * max(abs_nums2_0, abs_nums2_last)

        left, right = -mx, mx

        # Binary search for the smallest p such that count(p) >= k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left