class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {}
        for index, char in enumerate(s):
            last_occurrence[char] = index

        start = 0
        end = 0
        partition_sizes = []

        for index, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if index == end:
                partition_sizes.append(end - start + 1)
                start = index + 1

        return partition_sizes