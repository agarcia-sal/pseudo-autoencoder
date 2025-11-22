from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = 0
        previous = 0
        for current in target:
            if current > previous:
                operations += current - previous
            previous = current
        return operations