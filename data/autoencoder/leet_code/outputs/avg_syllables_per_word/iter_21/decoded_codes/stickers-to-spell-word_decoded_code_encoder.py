from collections import Counter, deque

class Solution:
    def minStickers(self, stickers, target):
        # Convert each sticker into a Counter of character frequencies
        stickers = [Counter(sticker) for sticker in stickers]
        # Sort stickers by the negative max frequency of any character to prioritize stickers with the most frequent character
        stickers.sort(key=lambda c: -max(c.values(), default=0))

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            for sticker in stickers:
                # If the first character of current_target is not in the sticker, skip to next sticker
                if current_target[0] not in sticker:
                    continue
                remaining = Counter(current_target)
                remaining.subtract(sticker)
                # Remove characters with zero or negative count
                new_target = ''.join(sorted(c * n for c, n in remaining.items() if n > 0))
                if not new_target:
                    return used_stickers + 1
                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1