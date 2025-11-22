class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {ch: i for i, ch in enumerate(s)}
        start = end = 0
        partition_sizes = []

        for i, ch in enumerate(s):
            end = max(end, last_occurrence[ch])
            if i == end:
                partition_sizes.append(end - start + 1)
                start = i + 1

        return partition_sizes