from collections import Counter

class Solution:
    def canDistribute(self, nums, quantity):
        count = list(Counter(nums).values())
        quantity.sort(reverse=True)

        def can_satisfy(index):
            if index == len(quantity):
                return True
            q = quantity[index]
            for i in range(len(count)):
                if count[i] >= q:
                    count[i] -= q
                    if can_satisfy(index + 1):
                        return True
                    count[i] += q
            return False

        return can_satisfy(0)