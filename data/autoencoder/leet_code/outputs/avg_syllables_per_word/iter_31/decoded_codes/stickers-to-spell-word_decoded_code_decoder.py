from collections import Counter, deque
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Convert each sticker into a frequency count mapping
        sticker_counts = [Counter(sticker) for sticker in stickers]
        # Sort stickers descendingly by the max frequency value among their characters
        sticker_counts.sort(key=lambda sc: max(sc.values()) if sc else 0, reverse=True)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            # If empty target reached, return the number of stickers used (for safety)
            if not current_target:
                return used_stickers

            current_target_count = Counter(current_target)

            for sticker in sticker_counts:
                # If the first character of current_target is not in the sticker, skip
                if current_target[0] not in sticker:
                    continue

                # Calculate remaining characters after using this sticker
                remaining = current_target_count - sticker
                # Create new_target string by sorted characters repeated by their positive counts
                new_target = ''.join(sorted(char * count for char, count in remaining.items()))

                if not new_target:
                    return used_stickers + 1

                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1