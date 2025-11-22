class Solution:
    def numFactoredBinaryTrees(self, list_of_numbers):
        MODULO_VALUE = 10**9 + 7
        list_of_numbers.sort()
        dp_mapping = self.initialize_dp_mapping(list_of_numbers)

        for index in range(len(list_of_numbers)):
            current_number = list_of_numbers[index]
            for inner_index in range(index):
                potential_factor = list_of_numbers[inner_index]
                if current_number % potential_factor == 0:
                    corresponding_factor = current_number // potential_factor
                    if corresponding_factor in dp_mapping:
                        product_count = dp_mapping[potential_factor] * dp_mapping[corresponding_factor]
                        dp_mapping[current_number] = (dp_mapping[current_number] + product_count) % MODULO_VALUE

        total_trees = self.sum_of_mapping_values(dp_mapping)
        result = total_trees % MODULO_VALUE
        return result

    def initialize_dp_mapping(self, list_of_numbers):
        dp_mapping = {}
        for number in list_of_numbers:
            dp_mapping[number] = 1
        return dp_mapping

    def sum_of_mapping_values(self, mapping):
        total_sum = 0
        for value in mapping.values():
            total_sum += value
        return total_sum