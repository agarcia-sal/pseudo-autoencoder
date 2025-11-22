from typing import List, Tuple
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], needs: List[int], special: List[List[int]]) -> int:
        valid_special = []
        for offer in special:
            # sum of offer items except last > 0
            if sum(offer[:-1]) > 0:
                # Cost of offer (last element) vs cost without offer
                offer_price = offer[-1]
                normal_price = sum(p * o for p, o in zip(price, offer[:-1]))
                if offer_price < normal_price:
                    valid_special.append(offer)

        @lru_cache(None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            # Cost without any special offer
            min_cost = sum(p * n for p, n in zip(price, current_needs))

            for offer in valid_special:
                new_needs = []
                for n, o in zip(current_needs, offer[:-1]):
                    diff = n - o
                    if diff < 0:
                        break
                    new_needs.append(diff)
                else:
                    # only if no break
                    cost_with_offer = offer[-1] + dfs(tuple(new_needs))
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))