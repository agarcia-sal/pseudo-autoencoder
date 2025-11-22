from bisect import bisect_right
from itertools import accumulate

class Solution:
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        flowers.sort()
        n = len(flowers)
        max_beauty = 0

        prefix_sum = [0] + list(accumulate(flowers))

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
                needed = target - flowers[n - i]
                remaining_flowers -= needed
                if remaining_flowers < 0:
                    break

            left, right = 0, n - i - 1

            while left <= right:
                mid = (left + right) // 2
                # Cost to raise all flowers[0..mid] to flowers[mid]
                cost = flowers[mid] * (mid + 1) - prefix_sum[mid + 1]
                if cost > remaining_flowers:
                    right = mid - 1
                else:
                    left = mid + 1

            if right >= 0:
                total = prefix_sum[right + 1]
                max_incomplete_flowers = flowers[right] + (remaining_flowers - (flowers[right] * (right + 1) - total)) // (right + 1)
                if max_incomplete_flowers >= target:
                    max_incomplete_flowers = target - 1
            else:
                max_incomplete_flowers = 0

            total_beauty = i * full + min(max_incomplete_flowers, target - 1) * partial
            if total_beauty > max_beauty:
                max_beauty = total_beauty

            remaining_flowers = newFlowers  # reset for next iteration

        return max_beauty