class Solution:
    def partitionLabels(self, s):
        last_occurrence = {}
        for i in range(len(s)):
            last_occurrence[s[i]] = i
        start = 0
        end = 0
        partition_sizes = []
        for i in range(len(s)):
            char = s[i]
            end = max(end, last_occurrence[char])
            if i == end:
                partition_sizes.append(end - start + 1)
                start = i + 1
        return partition_sizes