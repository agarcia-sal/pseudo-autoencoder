from collections import Counter, deque
from typing import List

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Convert each sticker to a Counter of character frequencies
        sticker_counts = [Counter(s) for s in stickers]
        # Sort stickers by the maximum frequency of any character in descending order
        sticker_counts.sort(key=lambda c: -max(c.values()) if c else 0)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            # Generate a Counter for current_target for reuse
            current_count = Counter(current_target)
            for sticker in sticker_counts:
                # Skip if first char of current_target not in sticker keys
                if current_target[0] not in sticker:
                    continue
                # Subtract sticker counts from current target counts
                remaining = current_count - sticker
                # Rebuild the string from the remaining counts sorted by character
                new_target = ''.join(char * remaining[char] for char in sorted(remaining))
                if not new_target:
                    return used_stickers + 1
                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))
        return -1