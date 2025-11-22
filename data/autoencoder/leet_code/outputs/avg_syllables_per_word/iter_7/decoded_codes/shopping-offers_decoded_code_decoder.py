from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # Filter specials: total items > 0 and special price < original price for those items
        filtered_special = []
        for offer in special:
            total_items = sum(offer[:-1])
            offer_price = offer[-1]
            original_price = sum(p * q for p, q in zip(price, offer[:-1]))
            if total_items > 0 and offer_price < original_price:
                filtered_special.append(offer)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, current_needs))

            for offer in filtered_special:
                new_needs = tuple(cn - q for cn, q in zip(current_needs, offer[:-1]))
                if all(x >= 0 for x in new_needs):
                    cost_with_offer = offer[-1] + dfs(new_needs)
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))