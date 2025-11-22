class Solution:
    def createSortedArray(self, instructions):
        MODULO = 10**9 + 1
        maximum = max(instructions) + 1
        bit_array = [0] * (maximum + 1)

        def update(index, value):
            while index <= maximum:
                bit_array[index] += value
                index += index & (-index)

        def query(index):
            total_sum = 0
            while index > 0:
                total_sum += bit_array[index]
                index -= index & (-index)
            return total_sum

        total_cost = 0
        for i, num in enumerate(instructions):
            less_than = query(num - 1)
            greater_than = i - query(num)
            cost = less_than if less_than <= greater_than else greater_than
            total_cost = (total_cost + cost) % MODULO
            update(num, 1)

        return total_cost