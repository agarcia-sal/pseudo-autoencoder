from functools import lru_cache
from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # Filter offers: sum of product counts > 0 AND offer price < sum(product price * count)
        filtered_special = []
        for offer in special:
            if sum(offer[:-1]) > 0 and offer[-1] < sum(p * c for p, c in zip(price, offer[:-1])):
                filtered_special.append(offer)
        special = filtered_special

        @lru_cache(None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            # Cost without any special offer
            min_cost = sum(p * n for p, n in zip(price, current_needs))

            for offer in special:
                new_needs = []
                for need_count, offer_count in zip(current_needs, offer[:-1]):
                    diff = need_count - offer_count
                    if diff < 0:
                        break
                    new_needs.append(diff)
                else:
                    # Only if all needs are non-negative after applying offer
                    cost_with_offer = offer[-1] + dfs(tuple(new_needs))
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))