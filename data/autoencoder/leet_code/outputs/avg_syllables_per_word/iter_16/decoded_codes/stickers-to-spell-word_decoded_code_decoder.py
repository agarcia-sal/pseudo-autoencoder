from collections import Counter, deque
from typing import List

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_counts = [Counter(s) for s in stickers]
        # Sort stickers by the maximum frequency character count descending for pruning
        sticker_counts.sort(key=lambda c: -max(c.values()) if c else 0)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used = queue.popleft()
            for sticker_map in sticker_counts:
                if current_target[0] not in sticker_map:
                    continue

                remaining = Counter(current_target)
                for ch in sticker_map:
                    remaining[ch] -= sticker_map[ch]
                    if remaining[ch] <= 0:
                        del remaining[ch]

                new_target = ''.join(sorted(ch * cnt for ch, cnt in remaining.items()))
                if not new_target:
                    return used + 1

                if new_target not in memo:
                    memo[new_target] = used + 1
                    queue.append((new_target, used + 1))

        return -1