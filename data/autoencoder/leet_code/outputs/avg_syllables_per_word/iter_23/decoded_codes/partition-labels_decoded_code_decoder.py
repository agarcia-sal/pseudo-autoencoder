from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        for i, character in enumerate(s):
            last_occurrence[character] = i

        start = 0
        end = 0
        partition_sizes = []

        for i, character in enumerate(s):
            if end < last_occurrence[character]:
                end = last_occurrence[character]

            if i == end:
                partition_size = end - start + 1
                partition_sizes.append(partition_size)
                start = i + 1

        return partition_sizes