import bisect

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k: int) -> int:
        nums2.sort()  # Ensure nums2 is sorted for bisect operations
        n = len(nums2)

        def count(p: int) -> int:
            cnt = 0
            for x in nums1:
                if x > 0:
                    # Count nums2[j] where nums2[j] <= p // x
                    bound = p // x
                    pos = bisect.bisect_right(nums2, bound)
                    cnt += pos
                elif x < 0:
                    # Count nums2[j] where nums2[j] >= ceil(p / x)
                    # Since x < 0, p/x is negative or positive, use bisect_left
                    # Compute division with careful rounding if needed
                    bound = (p + (-x - 1)) // x if x != 0 else 0  # Not used actually since x != 0
                    pos = bisect.bisect_left(nums2, (p + (-x - 1)) // x if x != 0 else 0)
                    # Simplify by using float division and then bisect_left
                    # Avoid float by directly handling integer division properly
                    # Because p and x are integers, p/x might be float, but bisect_left needs a value
                    # We'll just do p/x as float and bisect on that
                    # It's safer to do float division here:
                    pos = bisect.bisect_left(nums2, (p / x))
                    cnt += n - pos
                else:
                    # x == 0
                    cnt += n if p >= 0 else 0
            return cnt

        max_abs_nums1 = max(abs(nums1[0]), abs(nums1[-1]))
        max_abs_nums2 = max(abs(nums2[0]), abs(nums2[-1]))
        mx = max_abs_nums1 * max_abs_nums2

        # Binary search for the smallest value p such that count(p) >= k
        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left