from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        flipped = [0] * (n + 1)
        flip_state = 0
        for i in range(n):
            flip_state ^= flipped[i]
            if nums[i] == flip_state:
                if i + k > n:
                    return -1
                flip_state ^= 1
                flipped[i + k] ^= 1
                flip_count += 1
        return flip_count