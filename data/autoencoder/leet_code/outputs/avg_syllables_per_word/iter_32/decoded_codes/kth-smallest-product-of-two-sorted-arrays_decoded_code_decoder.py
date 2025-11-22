from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        nums2_sorted = nums2  # assume nums2 is sorted as per the pseudocode logic (no sort step is shown)
        n = len(nums2_sorted)

        def count(p: int) -> int:
            cnt = 0
            for x in nums1:
                if x > 0:
                    # count elements <= p // x in nums2
                    # use bisect_right to find position after last element <= p // x
                    # since we want number of y in nums2 with y <= p//x
                    val = p // x if x != 0 else (p if p >= 0 else float('-inf'))
                    pos = bisect_right(nums2_sorted, val)
                    cnt += pos
                elif x < 0:
                    # count elements >= ceil(p / x) in nums2
                    # since x < 0, p/x might not be an integer division,
                    # so we use p/x as float, then find first index of element not less than that value
                    val = p / x  # float division
                    pos = bisect_left(nums2_sorted, val)
                    cnt += n - pos
                else:
                    # x == 0
                    # if p >= 0 all pairs with x=0 will have product 0 <= p, otherwise 0
                    cnt += n if p >= 0 else 0
            return cnt

        # compute mx as MAX(|nums1[0]|, |nums1[-1]|)*MAX(|nums2[0]|, |nums2[-1]|)
        a = max(abs(nums1[0]), abs(nums1[-1]))
        b = max(abs(nums2[0]), abs(nums2[-1]))
        mx = a * b
        # Binary search for smallest number in range [-mx, mx] with count >= k
        left, right = -mx, mx

        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left