class Solution:
    def createSortedArray(self, instructions):
        MOD = 10**9 + 1
        MAX = max(instructions) + 1
        bit = [0] * MAX

        def update(idx, val):
            while idx < MAX:
                bit[idx] += val
                idx += idx & (-idx)

        def query(idx):
            total = 0
            while idx > 0:
                total += bit[idx]
                idx -= idx & (-idx)
            return total

        total_cost = 0
        for i, num in enumerate(instructions):
            less_than = query(num - 1)
            greater_than = i - query(num)
            cost = less_than if less_than < greater_than else greater_than
            total_cost = (total_cost + cost) % MOD
            update(num, 1)

        return total_cost