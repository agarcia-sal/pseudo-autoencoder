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

        for i in range(complete_gardens, n + 1):
            if i > 0:
                remaining_flowers -= target - flowers[n - i]
                if remaining_flowers < 0:
                    break

            left, right = 0, n - i - 1
            while left <= right:
                mid = (left + right) // 2
                cost = flowers[mid] * (mid + 1) - prefix_sum[mid + 1]
                if cost > remaining_flowers:
                    right = mid - 1
                else:
                    left = mid + 1

            if right >= 0:
                cost_used = flowers[right] * (right + 1) - prefix_sum[right + 1]
                max_incomplete_flowers = flowers[right] + (remaining_flowers - cost_used) // (right + 1)
                max_incomplete_flowers = min(max_incomplete_flowers, target - 1)
            else:
                max_incomplete_flowers = 0

            total_beauty = i * full + max_incomplete_flowers * partial
            if total_beauty > max_beauty:
                max_beauty = total_beauty

        return max_beauty