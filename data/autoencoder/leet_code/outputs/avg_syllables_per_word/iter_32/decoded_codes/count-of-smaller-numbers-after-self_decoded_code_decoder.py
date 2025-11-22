from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Coordinate compression: sort unique nums and assign a rank starting from 1
        sorted_nums = sorted(set(nums))
        rank = {}
        index = 0
        for value in sorted_nums:
            index += 1
            rank[value] = index

        bit = [0] * (len(sorted_nums) + 1)  # 1-based indexing Fenwick tree (BIT)

        def get_sum(idx: int) -> int:
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & (-idx)
            return res

        def update(idx: int, delta: int) -> None:
            while idx < len(bit):
                bit[idx] += delta
                idx += idx & (-idx)

        counts = []
        # Process nums from right to left
        for num in reversed(nums):
            r = rank[num]
            counts.append(get_sum(r - 1))  # count of elements smaller than num
            update(r, 1)

        return counts[::-1]