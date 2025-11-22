class Solution:
    def createSortedArray(self, instructions):
        MODULO = 10**9 + 7
        maximum = max(instructions) + 1
        BIT_array = [0] * maximum

        def update(index, value):
            while index < maximum:
                BIT_array[index] += value
                index += index & -index

        def query(index):
            total = 0
            while index > 0:
                total += BIT_array[index]
                index -= index & -index
            return total

        total_cost = 0
        for i, num in enumerate(instructions):
            less_than = query(num - 1)
            greater_than = i - query(num)
            cost = min(less_than, greater_than)
            total_cost = (total_cost + cost) % MODULO
            update(num, 1)

        return total_cost