from typing import List

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        MAX = max(instructions) + 1
        bit = [0] * (MAX + 1)  # 1-indexed Fenwick tree

        def update(idx: int, val: int) -> None:
            while idx <= MAX:
                bit[idx] += val
                idx += idx & -idx

        def query(idx: int) -> int:
            total = 0
            while idx > 0:
                total += bit[idx]
                idx -= idx & -idx
            return total

        total_cost = 0
        for i, num in enumerate(instructions):
            less_than = query(num - 1)
            greater_than = i - query(num)
            cost = min(less_than, greater_than)
            total_cost = (total_cost + cost) % MOD
            update(num, 1)

        return total_cost