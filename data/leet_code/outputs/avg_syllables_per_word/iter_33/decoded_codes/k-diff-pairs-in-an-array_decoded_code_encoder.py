class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        unique_pairs = 0
        for num in num_counts:
            if k == 0:
                if num_counts[num] > 1:
                    unique_pairs += 1
            else:
                if num + k in num_counts:
                    unique_pairs += 1
        return unique_pairs