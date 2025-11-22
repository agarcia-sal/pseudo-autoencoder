from collections import Counter

def can_distribute(nums, quantity):
    count = list(Counter(nums).values())
    quantity.sort(reverse=True)

    def can_satisfy(i):
        if i == len(quantity):
            return True
        for j in range(len(count)):
            if count[j] >= quantity[i]:
                count[j] -= quantity[i]
                if can_satisfy(i + 1):
                    return True
                count[j] += quantity[i]
        return False

    return can_satisfy(0)