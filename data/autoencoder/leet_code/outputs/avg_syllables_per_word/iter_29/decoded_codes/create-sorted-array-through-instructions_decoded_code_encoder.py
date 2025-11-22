class Solution:
    def createSortedArray(self, instructions):
        MODULO = 10**9 + 7
        MAXIMUM = max(instructions) + 1
        binary_indexed_tree = [0] * MAXIMUM

        def update(index, value):
            while index < MAXIMUM:
                binary_indexed_tree[index] += value
                index += index & (-index)

        def query(index):
            running_total = 0
            while index > 0:
                running_total += binary_indexed_tree[index]
                index -= index & (-index)
            return running_total

        total_cost = 0
        for i, num in enumerate(instructions):
            count_less_than = query(num - 1)
            count_greater_than = i - query(num)
            cost_value = count_less_than if count_less_than < count_greater_than else count_greater_than
            total_cost = (total_cost + cost_value) % MODULO
            update(num, 1)
        return total_cost