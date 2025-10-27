from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        rank = {}
        idx = 1
        for val in sorted_nums:
            rank[val] = idx
            idx += 1

        bit = [0] * (len(sorted_nums) + 1)

        def get_sum(i: int) -> int:
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def update(i: int, delta: int) -> None:
            while i < len(bit):
                bit[i] += delta
                i += i & -i

        counts = []
        for num in reversed(nums):
            r = rank[num]
            counts.append(get_sum(r - 1))
            update(r, 1)

        return counts[::-1]