import bisect

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        nums2.sort()
        n = len(nums2)

        def count(p):
            cnt = 0
            for x in nums1:
                if x > 0:
                    # count how many nums2[j] <= p//x
                    pos = bisect.bisect_right(nums2, p // x)
                    cnt += pos
                elif x < 0:
                    # count how many nums2[j] >= ceil(p/x)
                    # ceil division for negative x: careful with floor division properties
                    # since x < 0, p//x may need adjustment:
                    # but bisect_left(nums2, val) finds first position >= val, so use p/x normally
                    val = p / x
                    pos = bisect.bisect_left(nums2, val)
                    cnt += n - pos
                else:  # x == 0
                    if p >= 0:
                        cnt += n
            return cnt

        mx = max(abs(nums1[0]), abs(nums1[-1])) * max(abs(nums2[0]), abs(nums2[-1]))
        # Binary search in range [-mx, mx], find smallest p with count(p) >= k
        left, right = -mx, mx
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left