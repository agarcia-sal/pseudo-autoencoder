class Solution:
    def maximizeXor(self, list_of_numbers, list_of_queries):
        list_of_numbers.sort()
        indexed_sorted_queries = sorted(enumerate(list_of_queries), key=lambda x: x[1][1])
        result_list = [-1] * len(list_of_queries)
        trie_structure = {}
        current_index = 0

        for query_index, (number_xi, max_limit_mi) in indexed_sorted_queries:
            while current_index < len(list_of_numbers) and list_of_numbers[current_index] <= max_limit_mi:
                current_number = list_of_numbers[current_index]
                current_node = trie_structure
                for bit_position in range(31, -1, -1):
                    bit_value = (current_number >> bit_position) & 1
                    if bit_value not in current_node:
                        current_node[bit_value] = {}
                    current_node = current_node[bit_value]
                current_index += 1

            if not trie_structure:
                continue

            current_node = trie_structure
            maximum_xor_value = 0
            for bit_position in range(31, -1, -1):
                bit_value = (number_xi >> bit_position) & 1
                toggled_bit = 1 - bit_value
                if toggled_bit in current_node:
                    maximum_xor_value |= (1 << bit_position)
                    current_node = current_node[toggled_bit]
                else:
                    current_node = current_node[bit_value]

            result_list[query_index] = maximum_xor_value

        return result_list