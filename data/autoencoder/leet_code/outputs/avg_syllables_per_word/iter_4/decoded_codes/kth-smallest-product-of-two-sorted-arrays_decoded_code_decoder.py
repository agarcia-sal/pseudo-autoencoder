from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        nums1.sort()
        nums2.sort()

        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    v = p // x
                    # Since p/x might be float division for negative numbers in Python 3,
                    # we use integer division carefully. But p and x are int, so integer division is ok.
                    # bisect_right to find count of elements <= v
                    idx = bisect_right(nums2, v)
                    cnt += idx
                elif x < 0:
                    # For negative x, p / x flips inequality.
                    v = p // x
                    # need count of nums2 elements >= v
                    idx = bisect_left(nums2, v)
                    cnt += n - idx
                else:
                    # x == 0
                    # product is 0 always
                    if p >= 0:
                        cnt += n
            return cnt

        max_abs_nums1 = max(abs(nums1[0]), abs(nums1[-1]))
        max_abs_nums2 = max(abs(nums2[0]), abs(nums2[-1]))

        mx = max_abs_nums1 * max_abs_nums2

        left, right = -mx, mx + 1

        # binary search for smallest p with count(p) >= k
        while left < right:
            mid = (left + right) // 2
            c = count(mid)
            if c >= k:
                right = mid
            else:
                left = mid + 1

        return left