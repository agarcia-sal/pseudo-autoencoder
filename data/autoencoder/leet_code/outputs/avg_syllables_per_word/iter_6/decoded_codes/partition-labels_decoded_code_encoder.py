class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {c: i for i, c in enumerate(s)}
        start = end = 0
        partition_sizes = []
        for i, c in enumerate(s):
            end = max(end, last_occurrence[c])
            if i == end:
                partition_sizes.append(end - start + 1)
                start = i + 1
        return partition_sizes