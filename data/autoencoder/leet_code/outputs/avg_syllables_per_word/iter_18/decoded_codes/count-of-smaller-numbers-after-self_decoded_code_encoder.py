from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        rank = {val: i + 1 for i, val in enumerate(sorted_nums)}  # 1-based indexing for BIT

        bit = [0] * (len(sorted_nums) + 1)

        def get_sum(idx: int) -> int:
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & (-idx)
            return res

        def update(idx: int, delta: int):
            while idx < len(bit):
                bit[idx] += delta
                idx += idx & (-idx)

        counts = []
        for num in reversed(nums):
            r = rank[num]
            counts.append(get_sum(r - 1))
            update(r, 1)
        return counts[::-1]