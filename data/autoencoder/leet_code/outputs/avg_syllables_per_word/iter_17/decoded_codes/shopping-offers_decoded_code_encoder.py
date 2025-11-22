from functools import lru_cache
from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price_list: List[int], special_offers: List[List[int]], needs_list: List[int]) -> int:
        filtered_special_offers = []
        for offer in special_offers:
            sum_of_offer_items = sum(offer[:-1])
            sum_of_price_times_needs = sum(p * o for p, o in zip(price_list, offer[:-1]))
            if sum_of_offer_items > 0 and offer[-1] < sum_of_price_times_needs:
                filtered_special_offers.append(offer)
        special_OFFERS = filtered_special_offers

        @lru_cache(None)
        def dfs(needs_tuple: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price_list, needs_tuple))
            for offer in special_OFFERS:
                new_needs_list = [need - off for need, off in zip(needs_tuple, offer[:-1])]
                if all(need >= 0 for need in new_needs_list):
                    cost_with_offer = offer[-1] + dfs(tuple(new_needs_list))
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs_list))