class Solution:
    def shoppingOffers(self, price, special, needs):
        filtered_special = []
        for offer in special:
            total_items = sum(offer[:-1])
            total_price_without_offer = sum(p * c for p, c in zip(price, offer[:-1]))
            if total_items > 0 and offer[-1] < total_price_without_offer:
                filtered_special.append(offer)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(current_needs):
            min_cost = sum(p * n for p, n in zip(price, current_needs))
            for offer in filtered_special:
                new_needs = tuple(n - o for n, o in zip(current_needs, offer[:-1]))
                if all(x >= 0 for x in new_needs):
                    cost_with_offer = offer[-1] + dfs(new_needs)
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))