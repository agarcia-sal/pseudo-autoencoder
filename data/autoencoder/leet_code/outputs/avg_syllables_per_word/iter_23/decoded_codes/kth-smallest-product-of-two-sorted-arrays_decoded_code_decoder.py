from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        nums2.sort()

        def count(p: int) -> int:
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # Number of elements in nums2 <= p/x
                    pos = bisect_right(nums2, p // x) if x != 0 else (n if p >= 0 else 0)
                    cnt += pos
                elif x < 0:
                    # Number of elements in nums2 > p/x
                    pos = bisect_left(nums2, (p + (-1 if p % x else 0)) // x)  # careful with division floor
                    # but better: since x < 0, p/x decreases with x
                    # so count n - position for p/x
                    # Use float division, but since nums2 are integers and bisect works on ints,
                    # convert carefully by bisect_left at p/x, no rounding needed
                    # Since p/x might not be integer, we use bisect_left(nums2, p/x) and get n - pos
                    from math import floor
                    val = p / x
                    pos = bisect_left(nums2, val)
                    cnt += n - pos
                else:  # x == 0
                    cnt += len(nums2) if p >= 0 else 0
            return cnt

        # Compute mx as described (corrected to abs first and last element even if arrays unsorted)
        max1 = max(abs(nums1[0]), abs(nums1[-1]))
        max2 = max(abs(nums2[0]), abs(nums2[-1]))
        mx = max1 * max2

        # Binary search for the k-th smallest product in range [-mx, mx]
        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left