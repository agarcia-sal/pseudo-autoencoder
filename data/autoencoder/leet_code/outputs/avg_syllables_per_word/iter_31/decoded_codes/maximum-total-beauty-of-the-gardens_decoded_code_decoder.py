from typing import List


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        n = len(flowers)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + flowers[i]

        complete_gardens = 0
        # Count how many gardens are already full (>= target)
        for i in range(n - 1, -1, -1):
            if flowers[i] >= target:
                complete_gardens += 1
            else:
                break

        max_beauty = 0
        remaining_flowers = newFlowers
        max_incomplete_flowers = 0

        # Try making i gardens full (from current complete_gardens to total n)
        for i in range(complete_gardens, n + 1):
            if i > 0:
                # Subtract the flowers needed to bring the last i gardens up to target
                needed = target - flowers[n - i]
                remaining_flowers -= needed
                if remaining_flowers < 0:
                    break

            left, right = 0, n - i - 1
            pos = -1
            # Binary search for the maximum minimum flower count for incomplete gardens
            while left <= right:
                mid = (left + right) // 2
                # Flowers needed to raise all flowers from 0 to mid to flowers[mid]
                cost = flowers[mid] * (mid + 1) - prefix_sum[mid + 1]
                if cost > remaining_flowers:
                    right = mid - 1
                else:
                    pos = mid
                    left = mid + 1

            if pos >= 0:
                cost = flowers[pos] * (pos + 1) - prefix_sum[pos + 1]
                extra = remaining_flowers - cost
                max_incomplete_flowers = flowers[pos] + extra // (pos + 1)
                if max_incomplete_flowers >= target:
                    max_incomplete_flowers = target - 1
            else:
                max_incomplete_flowers = 0

            total_beauty = i * full + max_incomplete_flowers * partial
            if total_beauty > max_beauty:
                max_beauty = total_beauty

        return max_beauty