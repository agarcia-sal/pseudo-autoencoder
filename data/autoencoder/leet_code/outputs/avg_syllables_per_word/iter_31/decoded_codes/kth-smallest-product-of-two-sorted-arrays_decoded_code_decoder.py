from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums2.sort()  # Ensure nums2 is sorted for binary search

        def count(p: int) -> int:
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # number of elements in nums2 <= p // x
                    # Since division can produce float, need careful handling
                    # We want count of elements <= p // x
                    val = p // x
                    # bisect_right returns index of first element > val
                    cnt += bisect_right(nums2, val)
                elif x < 0:
                    # number of elements in nums2 where nums2[i] >= ceil(p / x)
                    # p / x could be float, but bisect_left finds first index >= val
                    val = p / x
                    idx = bisect_left(nums2, val)
                    cnt += n - idx
                else:
                    # x == 0: product is always 0
                    if p >= 0:
                        cnt += n
            return cnt

        # To find bounds for binary search:
        # max abs in nums1 at ends
        max_abs1 = max(abs(nums1[0]), abs(nums1[-1]))
        # max abs in nums2 at ends
        max_abs2 = max(abs(nums2[0]), abs(nums2[-1]))
        mx = max_abs1 * max_abs2

        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left