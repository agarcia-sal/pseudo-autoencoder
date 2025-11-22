from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        unique_numbers = set(nums)
        sorted_nums = sorted(unique_numbers)
        rank = {num: i + 1 for i, num in enumerate(sorted_nums)}

        bit = [0] * (len(sorted_nums) + 1)

        def get_sum(idx: int) -> int:
            result = 0
            while idx > 0:
                result += bit[idx]
                idx -= idx & (-idx)
            return result

        def update(idx: int, delta: int) -> None:
            while idx < len(bit):
                bit[idx] += delta
                idx += idx & (-idx)

        counts = []
        for num in reversed(nums):
            r = rank[num]
            counts.append(get_sum(r - 1))
            update(r, 1)
        counts.reverse()
        return counts