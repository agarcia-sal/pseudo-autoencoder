class Solution:
    def countSmaller(self, nums):
        sorted_unique_numbers = sorted(set(nums))
        rank_mapping = {}
        position_index = 1
        for value in sorted_unique_numbers:
            rank_mapping[value] = position_index
            position_index += 1

        binary_indexed_tree = [0] * (len(sorted_unique_numbers) + 1)

        def get_sum(index):
            result_sum = 0
            while index > 0:
                result_sum += binary_indexed_tree[index]
                index -= index & (-index)
            return result_sum

        def update(index, delta_value):
            while index < len(binary_indexed_tree):
                binary_indexed_tree[index] += delta_value
                index += index & (-index)

        counts_list = []
        for number in reversed(nums):
            current_rank = rank_mapping[number]
            smaller_count = get_sum(current_rank - 1)
            counts_list.append(smaller_count)
            update(current_rank, 1)

        return counts_list[::-1]