from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # Count nums2 elements <= p // x
                    cnt += bisect_right(nums2, p // x)
                elif x < 0:
                    # Count nums2 elements >= ceil(p / x)
                    # Since x < 0, p/x decreases as p increases.
                    # bisect_left(nums2, ceiling of p / x)
                    val = (p + (-x - 1)) // x if p % x != 0 else p // x  # careful division rounding
                    # actually can use p / x directly because bisect_left uses float comparison
                    # but to maintain correctness, just convert to float and do bisect_left with float
                    cnt += n - bisect_left(nums2, (p + (-1 if p % x != 0 else 0)) // x)
                    # However, to avoid confusion, using float conversion:
                    cnt += n - bisect_left(nums2, p / x)
                else:  # x == 0
                    cnt += n if p >= 0 else 0
            return cnt

        mx = max(abs(nums1[0]), abs(nums1[-1])) * max(abs(nums2[0]), abs(nums2[-1]))
        # We do binary search on [-mx, mx]
        left, right = -mx, mx

        # nums1 and nums2 should be sorted as implied by usage of bisect
        # If they are not, sort them
        nums1_sorted = nums1 if all(nums1[i] <= nums1[i+1] for i in range(len(nums1)-1)) else sorted(nums1)
        nums2_sorted = nums2 if all(nums2[i] <= nums2[i+1] for i in range(len(nums2)-1)) else sorted(nums2)

        nums1 = nums1_sorted
        nums2 = nums2_sorted

        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left