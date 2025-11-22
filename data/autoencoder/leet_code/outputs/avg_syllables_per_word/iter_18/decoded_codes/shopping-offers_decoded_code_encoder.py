from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        # Filter valid special offers
        filtered = []
        for offer in special:
            total_items = sum(offer[:-1])
            # Check if total items > 0 (offer provides items)
            if total_items <= 0:
                continue
            # Check if offer price is less than buying items individually
            individual_cost = sum(p * cnt for p, cnt in zip(price, offer[:-1]))
            if offer[-1] < individual_cost:
                filtered.append(offer)
        special = filtered

        @lru_cache(None)
        def dfs(needs_tuple: tuple[int, ...]) -> int:
            # Calculate cost without any special offer
            min_cost = sum(p * n for p, n in zip(price, needs_tuple))

            for offer in special:
                # Calculate new needs after applying offer
                new_needs = [n - o for n, o in zip(needs_tuple, offer[:-1])]
                if all(x >= 0 for x in new_needs):
                    cost_with_offer = offer[-1] + dfs(tuple(new_needs))
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))