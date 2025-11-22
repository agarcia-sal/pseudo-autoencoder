import bisect

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        nums2.sort()  # Ensure nums2 is sorted for bisect

        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # Count elements in nums2 <= p // x
                    # bisect_right returns the insertion position to the right of p//x
                    cnt += bisect.bisect_right(nums2, p // x)
                elif x < 0:
                    # Count elements in nums2 >= ceil(p / x)
                    # Since x < 0, p/x could be float; use math.ceil equivalent
                    # bisect_left returns the insertion position to the left of this value
                    # Since p/x can be float, we just do bisect_left(nums2, p / x),
                    # but we must note floor division is not used, p/x is float division
                    # Convert p/x to float and use bisect_left on float value
                    # Because nums2 is int, bisect will work with floats
                    pos = bisect.bisect_left(nums2, p / x)
                    cnt += n - pos
                else:
                    # x == 0
                    if p >= 0:
                        cnt += n
            return cnt

        mx1 = max(abs(nums1[0]), abs(nums1[-1]))
        mx2 = max(abs(nums2[0]), abs(nums2[-1]))
        mx = mx1 * mx2

        left, right = -mx, mx

        # Binary search for smallest p where count(p) >= k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left