class Solution:
    def partitionLabels(self, s):
        last_occurrence = {}
        for i in range(len(s)):
            char = s[i]
            last_occurrence[char] = i
        start = 0
        end = 0
        partition_sizes = []
        for i in range(len(s)):
            char = s[i]
            if end < last_occurrence[char]:
                end = last_occurrence[char]
            if i == end:
                partition_sizes.append(end - start + 1)
                start = i + 1
        return partition_sizes