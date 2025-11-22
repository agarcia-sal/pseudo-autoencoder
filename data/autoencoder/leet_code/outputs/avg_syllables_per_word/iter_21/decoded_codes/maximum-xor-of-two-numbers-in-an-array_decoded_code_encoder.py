class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        for i in range(31, -1, -1):
            max_xor <<= 1
            current_candidate = max_xor + 1
            prefixes = self.initializePrefixes(nums, i)
            for prefix in prefixes:
                if self.checkPrefixes(current_candidate, prefix, prefixes):
                    max_xor = current_candidate
                    break
        return max_xor

    def initializePrefixes(self, nums, i):
        prefixes = set()
        shift = 1 << i  # 2 ** i
        for num in nums:
            prefix = num // shift
            prefixes.add(prefix)
        return prefixes

    def checkPrefixes(self, current_candidate, prefix, prefixes):
        xor_value = current_candidate ^ prefix
        return xor_value in prefixes