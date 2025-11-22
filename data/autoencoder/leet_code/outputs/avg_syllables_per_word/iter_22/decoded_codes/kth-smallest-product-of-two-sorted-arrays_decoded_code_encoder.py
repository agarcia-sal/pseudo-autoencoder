import bisect

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        nums2.sort()  # Ensure nums2 is sorted for bisect operations

        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # Find rightmost index with value <= p/x
                    rhs = p / x
                    pos = bisect.bisect_right(nums2, rhs)
                    cnt += pos
                elif x < 0:
                    # Find leftmost index with value >= p/x
                    lhs = p / x
                    pos = bisect.bisect_left(nums2, lhs)
                    cnt += n - pos
                else:
                    # x == 0
                    if p >= 0:
                        cnt += n
            return cnt

        max_abs_nums1 = max(abs(nums1[0]), abs(nums1[-1]))
        max_abs_nums2 = max(abs(nums2[0]), abs(nums2[-1]))
        mx = max_abs_nums1 * max_abs_nums2

        # Binary search to find minimal p in [-mx, mx+1) s.t count(p) >= k
        left, right = -mx, mx + 1
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left