from collections import defaultdict
from math import inf

class Solution:
    def maximumBeauty(self, flowers):
        indices = defaultdict(list)
        prefix_sum = [0] * (len(flowers) + 1)
        for i in range(len(flowers)):
            value_at_index = flowers[i]
            prefix_sum[i + 1] = prefix_sum[i] + max(value_at_index, 0)
            indices[value_at_index].append(i)

        max_beauty = -inf
        for beauty_value, idx_list in indices.items():
            if len(idx_list) >= 2:
                first = idx_list[0]
                last = idx_list[-1]
                current_beauty = 2 * beauty_value + prefix_sum[last + 1] - prefix_sum[first + 1]
                if current_beauty > max_beauty:
                    max_beauty = current_beauty

        return max_beauty