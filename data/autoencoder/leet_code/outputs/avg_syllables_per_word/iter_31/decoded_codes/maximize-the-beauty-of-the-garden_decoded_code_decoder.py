from collections import defaultdict
import math

class Solution:
    def maximumBeauty(self, flowers):
        indices = defaultdict(list)
        n = len(flowers)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            val = flowers[i]
            prefix_sum[i + 1] = prefix_sum[i] + max(val, 0)
            indices[val].append(i)

        max_beauty = -math.inf
        for beauty_value, positions_list in indices.items():
            if len(positions_list) >= 2:
                first_position = positions_list[0]
                last_position = positions_list[-1]
                sum_between = prefix_sum[last_position] - prefix_sum[first_position + 1]
                current_beauty = 2 * beauty_value + sum_between
                if current_beauty > max_beauty:
                    max_beauty = current_beauty

        return max_beauty