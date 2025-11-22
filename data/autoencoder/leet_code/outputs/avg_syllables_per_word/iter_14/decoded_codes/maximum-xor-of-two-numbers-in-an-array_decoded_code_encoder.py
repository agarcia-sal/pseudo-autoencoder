class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        for bit_position in range(31, -1, -1):
            max_xor <<= 1
            current_candidate = max_xor | 1
            prefixes = set(num >> bit_position for num in nums)
            for prefix_element in prefixes:
                if (current_candidate ^ prefix_element) in prefixes:
                    max_xor = current_candidate
                    break
        return max_xor