class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0

        from collections import Counter
        num_counts = Counter(nums)

        unique_pairs = 0
        if k == 0:
            unique_pairs = sum(1 for count in num_counts.values() if count > 1)
        else:
            unique_pairs = sum(1 for num in num_counts if num + k in num_counts)

        return unique_pairs