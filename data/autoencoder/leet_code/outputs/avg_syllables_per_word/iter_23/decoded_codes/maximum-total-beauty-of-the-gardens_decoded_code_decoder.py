from typing import List

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        n = len(flowers)
        max_beauty = 0

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + flowers[i]

        complete_gardens = 0
        for i in range(n - 1, -1, -1):
            if flowers[i] >= target:
                complete_gardens += 1
            else:
                break

        remaining_flowers = newFlowers
        max_incomplete_flowers = 0

        # The max number of complete gardens ranges from complete_gardens up to n
        # because we may try to complete more gardens by using the newFlowers
        for i in range(complete_gardens, n + 1):
            # If i > 0, deduct flowers needed to complete the last i gardens from remaining_flowers
            if i > 0:
                required = 0
                # sum of flowers needed to make last i gardens full (at least target)
                # flowers sorted ascending, so last i gardens are flowers[n - i ... n-1]
                for j in range(n - i, n):
                    # we only add if flower[j] < target, otherwise garden already full so zero
                    if flowers[j] < target:
                        required += target - flowers[j]
                if required > remaining_flowers:
                    break
                remaining_flowers_i = remaining_flowers - required
            else:
                remaining_flowers_i = remaining_flowers

            # Binary search to find max minimum flower count in incomplete gardens (first n - i gardens)
            left, right = 0, n - i - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                # cost to raise flowers[0..mid] up to flowers[mid]
                # flowers are sorted ascending
                # total needed = flowers[mid]*(mid+1) - sum(flowers[0..mid])
                cost = flowers[mid] * (mid + 1) - prefix_sum[mid + 1]
                if cost <= remaining_flowers_i:
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1

            if res >= 0:
                # Calculate max_incomplete_flowers: raise all incomplete gardens to at least this value
                used = flowers[res] * (res + 1) - prefix_sum[res + 1]
                left_over = remaining_flowers_i - used
                # Distribute leftover flowers evenly to increase max_incomplete_flowers beyond flowers[res]
                max_incomplete_flowers = flowers[res] + left_over // (res + 1)
            else:
                max_incomplete_flowers = 0

            # Cannot exceed target - 1 on incomplete gardens
            max_incomplete_flowers = min(max_incomplete_flowers, target - 1)

            total_beauty = i * full + max_incomplete_flowers * partial
            if total_beauty > max_beauty:
                max_beauty = total_beauty

        return max_beauty