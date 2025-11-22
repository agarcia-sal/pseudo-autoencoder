class Solution:
    def partitionLabels(self, s):
        last_occurrence = {}
        for i, c in enumerate(s):
            last_occurrence[c] = i

        start = 0
        end = 0
        partition_sizes = []

        for i, c in enumerate(s):
            if last_occurrence[c] > end:
                end = last_occurrence[c]
            if i == end:
                partition_sizes.append(end - start + 1)
                start = i + 1

        return partition_sizes