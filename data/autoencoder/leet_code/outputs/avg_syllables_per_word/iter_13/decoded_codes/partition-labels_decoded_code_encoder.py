class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {}
        for i, character in enumerate(s):
            last_occurrence[character] = i
        start = end = 0
        partition_sizes = []
        for i, character in enumerate(s):
            if last_occurrence[character] > end:
                end = last_occurrence[character]
            if i == end:
                partition_sizes.append(end - start + 1)
                start = i + 1
        return partition_sizes