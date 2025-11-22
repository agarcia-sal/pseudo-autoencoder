class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        for i in range(31, -1, -1):
            max_xor <<= 1
            current_candidate = max_xor | 1
            prefixes = {num >> i for num in nums}
            if any((current_candidate ^ prefix) in prefixes for prefix in prefixes):
                max_xor = current_candidate
        return max_xor