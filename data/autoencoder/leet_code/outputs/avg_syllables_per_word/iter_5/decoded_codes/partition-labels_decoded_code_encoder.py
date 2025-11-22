class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {char: i for i, char in enumerate(s)}
        start = 0
        end = 0
        partition_sizes = []
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                partition_sizes.append(end - start + 1)
                start = i + 1
        return partition_sizes