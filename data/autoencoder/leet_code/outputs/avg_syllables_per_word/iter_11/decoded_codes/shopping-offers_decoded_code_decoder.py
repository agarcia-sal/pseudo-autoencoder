from functools import cache

class Solution:
    def shoppingOffers(self, price, special, needs):
        filtered_special = []
        for offer in special:
            if sum(offer[:-1]) > 0 and offer[-1] < sum(p * q for p, q in zip(price, offer[:-1])):
                filtered_special.append(offer)

        @cache
        def dfs(needs):
            min_cost = sum(p * q for p, q in zip(price, needs))
            for offer in filtered_special:
                new_needs = [need - off for need, off in zip(needs, offer[:-1])]
                if all(x >= 0 for x in new_needs):
                    min_cost = min(min_cost, offer[-1] + dfs(tuple(new_needs)))
            return min_cost

        return dfs(tuple(needs))