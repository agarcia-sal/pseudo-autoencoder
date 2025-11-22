from collections import defaultdict
from math import inf

class Solution:
    def maximumBeauty(self, flowers):
        beauty_indices = defaultdict(list)  # Maps each beauty value to a list of indices
        prefix_sum = [0] * (len(flowers) + 1)

        for i, val in enumerate(flowers):
            prefix_sum[i + 1] = prefix_sum[i] + max(val, 0)
            beauty_indices[val].append(i)

        max_beauty = -inf
        for beauty, indices in beauty_indices.items():
            if len(indices) >= 2:
                first, last = indices[0], indices[-1]
                current_beauty = 2 * beauty + prefix_sum[last] - prefix_sum[first + 1]
                if current_beauty > max_beauty:
                    max_beauty = current_beauty

        return max_beauty