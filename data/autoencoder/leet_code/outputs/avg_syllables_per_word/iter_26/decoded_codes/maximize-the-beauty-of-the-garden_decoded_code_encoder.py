from collections import defaultdict
from math import inf

class Solution:
    def maximumBeauty(self, flowers):
        indices = defaultdict(list)
        prefix_sum = [0] * (len(flowers) + 1)

        for index in range(len(flowers)):
            element_value = flowers[index]
            prefix_sum[index + 1] = prefix_sum[index] + max(element_value, 0)
            indices[element_value].append(index)

        max_beauty = -inf

        for beauty_value, positions in indices.items():
            if len(positions) >= 2:
                first = positions[0]
                last = positions[-1]
                current_beauty = 2 * beauty_value + prefix_sum[last] - prefix_sum[first + 1]
                if current_beauty > max_beauty:
                    max_beauty = current_beauty

        return max_beauty