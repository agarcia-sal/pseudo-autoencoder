from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        # nums1 and nums2 are assumed sorted non-empty lists of integers
        # count(p) returns how many products nums1[i]*nums2[j] <= p
        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # number of elements in nums2 with value <= p//x (integer division for proper indexing)
                    # since nums2 is sorted, use bisect_right
                    cnt += bisect_right(nums2, p // x)
                elif x < 0:
                    # number of elements in nums2 with value >= ceil(p/x)
                    # which is equivalent to n - number of elements < ceil(p/x)
                    # ceil division careful:
                    val = (p + (-x) - 1)//x if x < 0 else p // x  # better to use float division and math.ceil
                    # but p/x may be float; so use p/x and bisect_left accordingly
                    # p/x for negative x is negative division; use float for proper comparison
                    # so just do p/x float then bisect accordingly

                    target = p / x  # float division since x < 0
                    # Need elements in nums2 >= target
                    # number elements < target = bisect_left(nums2, target)
                    cnt += n - bisect_left(nums2, target)
                else:  # x == 0
                    if p >= 0:
                        cnt += n  # all products zero <= p if p >= 0, else zero
            return cnt

        # calculate max absolute product bound for binary search
        max_abs_num1 = max(abs(nums1[0]), abs(nums1[-1]))
        max_abs_num2 = max(abs(nums2[0]), abs(nums2[-1]))
        mx = max_abs_num1 * max_abs_num2

        # binary search for the k-th smallest product in range [-mx, mx]
        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left