from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(sorted_nums)}
        bit = [0] * (len(sorted_nums) + 1)

        def get_sum(idx: int) -> int:
            result = 0
            while idx > 0:
                result += bit[idx]
                idx -= idx & -idx
            return result

        def update(idx: int, delta: int) -> None:
            n = len(bit)
            while idx < n:
                bit[idx] += delta
                idx += idx & -idx

        counts = []
        for num in reversed(nums):
            r = rank[num]
            counts.append(get_sum(r - 1))
            update(r, 1)

        counts.reverse()
        return counts