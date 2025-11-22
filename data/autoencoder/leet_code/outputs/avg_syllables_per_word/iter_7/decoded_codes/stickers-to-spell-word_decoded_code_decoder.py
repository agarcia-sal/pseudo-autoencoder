from collections import deque, Counter
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_counts = [Counter(s) for s in stickers]
        sticker_counts.sort(key=lambda c: max(c.values()), reverse=True)

        queue = deque()
        queue.append((target, 0))
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            current_count = Counter(current_target)

            for sticker in sticker_counts:
                if current_target[0] not in sticker:
                    continue

                remaining = current_count - sticker
                if not remaining:
                    return used_stickers + 1

                new_target = ''.join(sorted(remaining.elements()))
                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1