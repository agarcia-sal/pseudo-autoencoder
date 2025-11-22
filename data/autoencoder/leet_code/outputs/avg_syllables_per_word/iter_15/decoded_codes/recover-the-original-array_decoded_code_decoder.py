from collections import Counter

class Solution:
    def recoverArray(self, nums):
        nums.sort()
        n = len(nums)
        first = nums[0]
        for i in range(1, n):
            if (nums[i] - first) % 2 != 0:
                continue
            k = (nums[i] - first) // 2
            if k <= 0 or first + 2 * k != nums[i]:
                continue
            count = Counter(nums)
            arr = []
            for x in nums:
                if count[x] == 0:
                    continue
                if count.get(x + 2 * k, 0) == 0:
                    break
                arr.append(x + k)
                count[x] -= 1
                count[x + 2 * k] -= 1
            if len(arr) == n // 2:
                return arr
        return []