class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        for i in range(31, -1, -1):
            max_xor <<= 1
            current_candidate = max_xor + 1
            prefixes = set()
            for num in nums:
                prefixes.add(num >> i)
            for p in prefixes:
                if current_candidate ^ p in prefixes:
                    max_xor = current_candidate
                    break
        return max_xor