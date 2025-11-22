from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count(p: int) -> int:
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # count how many nums2[j] <= p//x (considering division carefully)
                    # Use bisect_right for count of elements <= p/x
                    target = p // x
                    cnt += bisect_right(nums2, target)
                elif x < 0:
                    # count how many nums2[j] >= ceil(p/x)
                    # For negative x, p/x can be -inf to +inf, use bisect_left
                    # number of elements >= ceil(p/x) = n - bisect_left(nums2, ceil(p/x))
                    # Careful with division and ceil for negatives
                    # For exact division handling, use integer division and adjust:
                    # Instead, just use bisect_left(nums2, (p + x - 1)//x) when x<0
                    # But better to use float division with math.ceil for correctness
                    from math import ceil
                    target = ceil(p / x)
                    cnt += n - bisect_left(nums2, target)
                else:
                    # x == 0
                    # if p >= 0, all products 0*x are 0 <= p so count += n else 0
                    if p >= 0:
                        cnt += n
            return cnt

        mx = max(abs(nums1[0]), abs(nums1[-1]))
        mx *= max(abs(nums2[0]), abs(nums2[-1]))

        # Binary search over range [-mx, mx]
        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left