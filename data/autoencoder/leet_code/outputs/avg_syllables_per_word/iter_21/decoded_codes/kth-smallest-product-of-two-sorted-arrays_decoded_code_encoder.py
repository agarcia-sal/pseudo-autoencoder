from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        # nums1 and nums2 are assumed to be sorted arrays as per the logic implied by binary searches
        def count(p):
            cnt = 0
            n = len(nums2)
            for x in nums1:
                if x > 0:
                    # Number of elements y in nums2 with y <= p/x
                    cnt += bisect_right(nums2, p // x)
                elif x < 0:
                    # Number of elements y in nums2 with y >= ceil(p/x) = p//x if divisible else +1 
                    # Because division in python floor, we use bisect_left for p//x
                    # since for negative x, products decrease as y increases
                    cnt += n - bisect_left(nums2, (p + (-x + 1)) // x if p % x != 0 else p // x)
                else:
                    # x == 0
                    if p >= 0:
                        cnt += n
            return cnt

        mx = max(abs(nums1[0]), abs(nums1[-1])) * max(abs(nums2[0]), abs(nums2[-1]))

        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left