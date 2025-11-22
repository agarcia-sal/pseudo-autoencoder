from functools import lru_cache

class Solution:
    def shoppingOffers(self, price, special, needs):
        filtered_special = []
        for offer in special:
            if sum(offer[:-1]) > 0 and offer[-1] < sum(p * o for p, o in zip(price, offer[:-1])):
                filtered_special.append(offer)

        @lru_cache(None)
        def dfs(needs):
            min_cost = sum(p * n for p, n in zip(price, needs))
            for offer in filtered_special:
                new_needs = []
                for i in range(len(needs)):
                    new_needs.append(needs[i] - offer[i])
                if all(n >= 0 for n in new_needs):
                    possible_cost = offer[-1] + dfs(tuple(new_needs))
                    if possible_cost < min_cost:
                        min_cost = possible_cost
            return min_cost

        return dfs(tuple(needs))