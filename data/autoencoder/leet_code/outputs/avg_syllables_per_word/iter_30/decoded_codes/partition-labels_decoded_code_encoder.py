class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {}
        for index, character in enumerate(s):
            last_occurrence[character] = index

        start = 0
        end = 0
        partition_sizes = []
        for index, character in enumerate(s):
            if end < last_occurrence[character]:
                end = last_occurrence[character]
            if index == end:
                partition_sizes.append(end - start + 1)
                start = index + 1

        return partition_sizes