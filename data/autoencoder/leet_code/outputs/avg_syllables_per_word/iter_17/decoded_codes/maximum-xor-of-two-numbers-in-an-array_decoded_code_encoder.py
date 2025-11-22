class Solution:
    def findMaximumXOR(self, list_of_numbers):
        maximum_xor = 0
        for bit_position in range(31, -1, -1):
            maximum_xor <<= 1  # multiply by 2
            current_candidate = maximum_xor + 1
            prefixes = self.CreatePrefixSet(list_of_numbers, bit_position)
            for prefix_element in prefixes:
                if (current_candidate ^ prefix_element) in prefixes:
                    maximum_xor = current_candidate
                    break
        return maximum_xor

    def CreatePrefixSet(self, list_of_numbers, bit_position):
        prefix_set = set()
        shift = 1 << bit_position  # 2 ** bit_position
        for number in list_of_numbers:
            shifted_prefix = number // shift
            prefix_set.add(shifted_prefix)
        return prefix_set