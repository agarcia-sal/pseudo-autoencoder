from collections import Counter, deque
from typing import List

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Convert each sticker to a frequency counter
        sticker_counts = [Counter(sticker) for sticker in stickers]
        # Sort stickers by the max frequency value descending
        sticker_counts.sort(key=lambda c: max(c.values(), default=0), reverse=True)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            current_target_first_char = current_target[0]

            for sticker in sticker_counts:
                if current_target_first_char not in sticker:
                    continue

                remaining = Counter(current_target) - sticker
                # Form new target string sorted ascending by character
                # remaining.elements() yields chars repeated by their counts
                new_target = ''.join(sorted(remaining.elements()))

                if not new_target:
                    return used_stickers + 1

                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1