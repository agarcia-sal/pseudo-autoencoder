from collections import Counter
from typing import List

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        count = list(Counter(nums).values())
        quantity.sort(reverse=True)

        def can_satisfy(index: int) -> bool:
            if index == len(quantity):
                return True
            for i in range(len(count)):
                if count[i] >= quantity[index]:
                    count[i] -= quantity[index]
                    if can_satisfy(index + 1):
                        return True
                    count[i] += quantity[index]
            return False

        return can_satisfy(0)