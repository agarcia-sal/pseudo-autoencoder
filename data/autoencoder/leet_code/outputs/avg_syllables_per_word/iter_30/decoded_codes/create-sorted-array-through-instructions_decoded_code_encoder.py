class Solution:
    def createSortedArray(self, instructions: list[int]) -> int:
        MODULO = 10**9 + 7
        maximum = max(instructions) + 1
        BIT = [0] * maximum

        def update(index: int, value: int) -> None:
            while index < maximum:
                BIT[index] += value
                index += index & -index

        def query(index: int) -> int:
            total = 0
            while index > 0:
                total += BIT[index]
                index -= index & -index
            return total

        total_cost = 0
        for i, num in enumerate(instructions):
            less_than = query(num - 1)
            greater_than = i - query(num)
            cost = less_than if less_than < greater_than else greater_than
            total_cost += cost
            total_cost %= MODULO
            update(num, 1)

        return total_cost