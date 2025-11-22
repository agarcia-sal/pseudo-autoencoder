from bisect import bisect_left

class Solution:
    def countSmaller(self, list_of_numbers):
        sorted_unique_numbers = self.create_sorted_unique_list(list_of_numbers)
        rank_dictionary = self.create_rank_dictionary(sorted_unique_numbers)
        size = len(sorted_unique_numbers) + 1
        binary_indexed_tree = self.initialize_bit(size)

        def get_sum(index):
            result = 0
            while index > 0:
                result += binary_indexed_tree[index]
                index -= index & (-index)
            return result

        def update(index, delta):
            while index < size:
                binary_indexed_tree[index] += delta
                index += index & (-index)

        counts_list = []
        for number in reversed(list_of_numbers):
            current_rank = rank_dictionary[number]
            counts_list.append(get_sum(current_rank - 1))
            update(current_rank, 1)
        return counts_list[::-1]

    def create_sorted_unique_list(self, list_of_numbers):
        return sorted(set(list_of_numbers))

    def create_rank_dictionary(self, sorted_unique_numbers):
        # Using dict comprehension with enumerate starting rank at 1
        return {num: i + 1 for i, num in enumerate(sorted_unique_numbers)}

    def initialize_bit(self, size):
        # BIT uses 1-based indexing; size includes one extra element
        return [0] * size