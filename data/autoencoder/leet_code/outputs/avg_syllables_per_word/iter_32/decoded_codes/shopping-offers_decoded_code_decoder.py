from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # Filter specials: keep only those with positive total items and cost less than direct purchase
        filtered_special = []
        price_sum = sum(price[i] * offer_count for i, offer_count in enumerate([0]*len(price)))  # initial zero, for type clarity

        for offer in special:
            if sum(offer[:-1]) > 0:
                direct_cost = sum(p * c for p, c in zip(price, offer[:-1]))
                if offer[-1] < direct_cost:
                    filtered_special.append(offer)

        special = filtered_special

        memo = {}

        def dfs(current_needs: Tuple[int, ...]) -> int:
            if current_needs in memo:
                return memo[current_needs]

            # Cost without any specials, direct buy
            min_cost = sum(p * n for p, n in zip(price, current_needs))

            for offer in special:
                new_needs = []
                for n, o in zip(current_needs, offer[:-1]):
                    diff = n - o
                    if diff < 0:
                        # Cannot use this offer as it requires more items than needed
                        break
                    new_needs.append(diff)
                else:
                    # Offer is applicable
                    cost_with_offer = offer[-1] + dfs(tuple(new_needs))
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer

            memo[current_needs] = min_cost
            return min_cost

        return dfs(tuple(needs))