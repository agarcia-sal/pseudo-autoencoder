from functools import lru_cache
from typing import List, Tuple


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            sum_of_offer_items = sum(offer[:-1])
            sum_of_regular_price = 0
            for i in range(len(price)):
                sum_of_regular_price += price[i] * offer[i]
            if sum_of_offer_items > 0 and offer[-1] < sum_of_regular_price:
                filtered_special.append(offer)
        special = filtered_special

        @lru_cache(None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            min_cost = 0
            for i in range(len(price)):
                min_cost += price[i] * current_needs[i]

            for offer in special:
                new_needs = []
                for i in range(len(current_needs)):
                    new_need = current_needs[i] - offer[i]
                    new_needs.append(new_need)
                if all(n >= 0 for n in new_needs):
                    candidate_cost = offer[-1] + dfs(tuple(new_needs))
                    if candidate_cost < min_cost:
                        min_cost = candidate_cost
            return min_cost

        return dfs(tuple(needs))