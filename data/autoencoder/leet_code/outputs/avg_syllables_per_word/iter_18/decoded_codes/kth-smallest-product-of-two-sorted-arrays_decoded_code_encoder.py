from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        nums2_sorted = sorted(nums2)
        n = len(nums2_sorted)

        def count(p: int) -> int:
            cnt = 0
            for x in nums1:
                if x > 0:
                    # number of y in nums2 such that x*y <= p
                    cnt += bisect_right(nums2_sorted, p // x)
                elif x < 0:
                    # number of y in nums2 such that x*y <= p, x<0
                    # This is count of y > p/x
                    cnt += n - bisect_left(nums2_sorted, (p + (-1 if p % x else 0)) // x)  # adjusted for floor division if needed
                    # Above line can be simplified to:
                    # cnt += n - bisect_left(nums2_sorted, p // x)
                    # because integer division in Python is floor division by default
                    # So let's keep it as:
                    # cnt += n - bisect_left(nums2_sorted, p // x)
                    # Removing previous adjustment line to avoid confusion
                else:
                    # x == 0
                    if p >= 0:
                        cnt += n
            return cnt

        absolute_max_first_element_nums1 = abs(nums1[0])
        absolute_max_last_element_nums1 = abs(nums1[-1])
        absolute_max_first_element_nums2 = abs(nums2[0])
        absolute_max_last_element_nums2 = abs(nums2[-1])

        mx = max(absolute_max_first_element_nums1, absolute_max_last_element_nums1) * \
             max(absolute_max_first_element_nums2, absolute_max_last_element_nums2)

        # We will bisect on the value range [-mx, mx]
        # Create a range but not as list, we use integer limits directly in binary search
        low, high = -mx, mx
        while low < high:
            mid = (low + high) // 2
            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low