from collections import Counter
from typing import List

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        count = list(Counter(nums).values())
        quantity.sort(reverse=True)

        def can_satisfy(index: int) -> bool:
            if index == len(quantity):
                return True
            need = quantity[index]
            for i in range(len(count)):
                if count[i] >= need:
                    count[i] -= need
                    if can_satisfy(index + 1):
                        return True
                    count[i] += need
            return False

        return can_satisfy(0)