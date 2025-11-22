from collections import Counter, deque
from typing import List, Tuple

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Transform each sticker into a Counter of character frequencies
        sticker_counters = [Counter(sticker) for sticker in stickers]
        # Sort stickers so that the one with the highest count of any character comes first
        sticker_counters.sort(key=lambda sc: max(sc.values()) if sc else 0, reverse=True)

        queue = deque()
        queue.append((target, 0))
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()

            for sticker_counter in sticker_counters:
                # If the first character of current_target is not in the sticker, skip this sticker
                if current_target[0] not in sticker_counter:
                    continue

                remaining = Counter(current_target)
                # Subtract the sticker's character counts from the remaining target characters
                remaining.subtract(sticker_counter)

                # Construct the new target string with only positive counts, sorted
                new_target = ''.join(sorted(ch * cnt for ch, cnt in remaining.items() if cnt > 0))

                if not new_target:
                    return used_stickers + 1

                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1