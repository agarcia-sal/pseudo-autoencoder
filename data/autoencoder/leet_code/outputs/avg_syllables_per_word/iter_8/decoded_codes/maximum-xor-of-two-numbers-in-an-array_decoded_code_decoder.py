class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        for i in range(31, -1, -1):
            max_xor = max_xor * 2
            current_candidate = max_xor + 1
            prefixes = set()
            for num in nums:
                prefix = num // (2 ** i)
                prefixes.add(prefix)
            for prefix in prefixes:
                needed = current_candidate ^ prefix
                if needed in prefixes:
                    max_xor = current_candidate
                    break
        return max_xor