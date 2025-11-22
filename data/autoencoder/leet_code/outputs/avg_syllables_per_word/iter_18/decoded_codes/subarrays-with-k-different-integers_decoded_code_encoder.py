from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMostKDistinct(t: int) -> int:
            count = defaultdict(int)
            left = 0
            result = 0
            for right in range(len(nums)):
                count[nums[right]] += 1
                while len(count) > t:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                result += right - left + 1
            return result

        result_with_k = atMostKDistinct(k)
        result_with_k_minus_one = atMostKDistinct(k - 1)
        return result_with_k - result_with_k_minus_one