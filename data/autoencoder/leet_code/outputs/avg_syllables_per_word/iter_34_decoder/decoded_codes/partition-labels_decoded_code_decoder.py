from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i

        start = 0
        end = 0
        partition_sizes = []

        for i, char in enumerate(s):
            if end < last_occurrence[char]:
                end = last_occurrence[char]
            if i == end:
                partition_sizes.append(end - start + 1)
                start = i + 1

        return partition_sizes