from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        nums2_sorted = nums2  # nums2 is expected sorted in the pseudocode context

        def count(p):
            cnt = 0
            n = len(nums2_sorted)
            for x in nums1:
                if x > 0:
                    # count how many nums2 elements <= p // x
                    cnt += bisect_right(nums2_sorted, p // x)
                elif x < 0:
                    # count how many nums2 elements >= ceil(p / x)
                    # bisect_left(nums2_sorted, value) returns index of left insertion point
                    # number of elements >= value = n - bisect_left(nums2_sorted, value)
                    # as p / x is negative / negative might be positive or negative, be careful with division,
                    # use float division and math.ceil to handle properly
                    val = (p + (-1 if p % x != 0 else 0)) // x if p % x != 0 else p // x
                    # but integer division truncates towards minus infinity in Python
                    # safer to use float division with ceiling
                    from math import ceil
                    val = ceil(p / x)
                    cnt += n - bisect_left(nums2_sorted, val)
                else:
                    if p >= 0:
                        cnt += n
            return cnt

        mx = max(abs(nums1[0]), abs(nums1[-1])) * max(abs(nums2[0]), abs(nums2[-1]))

        # We want to find the smallest integer 'result' in [-mx, mx] such that count(result) >= k
        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left