from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        nums2.sort()
        n = len(nums2)

        def count(p):
            cnt = 0
            for x in nums1:
                if x > 0:
                    # Find rightmost index with nums2[i] <= p/x
                    val = p // x if p >= 0 else (p - (x - 1)) // x
                    pos = bisect_right(nums2, val)
                    cnt += pos
                elif x < 0:
                    # Find leftmost index with nums2[i] >= ceil(p/x)
                    # ceil(p/x) = -((-p)//x) if x < 0
                    # But to avoid float division, use formula
                    val = p // x if (p % x == 0) else (p // x) + 1
                    pos = bisect_left(nums2, val)
                    cnt += n - pos
                else:
                    if p >= 0:
                        cnt += n
            return cnt

        abs1 = max(abs(nums1[0]), abs(nums1[-1]))
        abs2 = max(abs(nums2[0]), abs(nums2[-1]))
        mx = abs1 * abs2

        left, right = -mx, mx + 1
        while left < right:
            mid = (left + right) // 2
            c = count(mid)
            if c >= k:
                right = mid
            else:
                left = mid + 1
        return left